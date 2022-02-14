from typing import Dict, List


class JobNode:
    def __init__(self, job: str) -> None:
        self.job = job
        self.dependencies: List[JobNode] = []
        self.num_of_prerequisites = 0


class JobGraph:
    def __init__(self, jobs: List[str]) -> None:
        self.nodes: List[JobNode] = []
        self.graph: Dict[str, JobNode] = {}
        for job in jobs:
            self.add_node(job)

    def add_node(self, job: str) -> None:
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def add_dependency(self, job: str, dependency: str) -> None:
        job_node = self.get_node(job)
        dependency_node = self.get_node(dependency)
        job_node.dependencies.append(dependency_node)
        dependency_node.num_of_prerequisites += 1

    def get_node(self, job: str) -> JobNode:
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]


def topological_sort(jobs: List[str], dependencies: List[str]) -> List[JobNode]:
    job_graph = create_job_graph(jobs, dependencies)
    return get_ordered_jobs(job_graph)


def create_job_graph(jobs: List[str], dependencies: List[str]) -> JobGraph:
    graph = JobGraph(jobs)
    for job, dependency in dependencies:
        graph.add_dependency(job, dependency)
    return graph


def get_ordered_jobs(graph: JobGraph) -> List[JobNode]:
    ordered_jobs = []
    nodes_with_no_prerequisites = list(
        filter(lambda node: node.num_of_prerequisites == 0, graph.nodes))
    while len(nodes_with_no_prerequisites):
        node = nodes_with_no_prerequisites.pop()
        ordered_jobs.append(node.job)
        remove_dependencies(node, nodes_with_no_prerequisites)
    graph_has_edges = any(node.num_of_prerequisites for node in graph.nodes)
    return [] if graph_has_edges else ordered_jobs


def remove_dependencies(node: JobNode,
                        nodes_with_no_prerequisites: List[JobNode]) -> None:
    while len(node.dependencies):
        dependency = node.dependencies.pop()
        dependency.num_of_prerequisites -= 1
        if dependency.num_of_prerequisites == 0:
            nodes_with_no_prerequisites.append(dependency)
