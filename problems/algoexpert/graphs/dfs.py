from typing import List
from typing_extensions import Self


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[Node] = []

    def add_child(self, name: str) -> Self:
        self.children.append(Node(name))
        return self

    def depth_first_search(self, names: List[str]) -> List[str]:
        names.append(self.name)
        for child in self.children:
            child.depth_first_search(names)
        return names


A = Node("A")
B = Node("B")
A.add_child("B").add_child("C").add_child("D")
print(A.name)
print(A.depth_first_search([]))
