from typing import List


class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.children: List[Node] = []

    def add_child(self, name: str):
        self.children.append(Node(name))
        return self

    def breadth_first_search(self, names: List[str]) -> List[str]:
        queue: List[Node] = [self]
        while len(queue) > 0:
            curr_node = queue.pop(0)
            names.append(curr_node.name)
            for child in curr_node.children:
                queue.append(child)
        return names


A = Node("A")
A.add_child("B").add_child("C").add_child("D").add_child("E")
A.add_child("F").add_child("G").add_child("H").add_child("I")
A.add_child("J").add_child("K")
print(A.breadth_first_search([]))
