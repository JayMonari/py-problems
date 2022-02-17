from typing import Optional


class Node:
    def __init__(self, value: int, _next=None, _prev=None):
        self.value: int = value
        self.next: Optional[Node] = _next
        self.prev: Optional[Node] = _prev


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def set_head(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_before(self.head, node)

    def set_tail(self, node: Node) -> None:
        if self.tail is None:
            self.set_head(node)
            return
        self.insert_after(self.tail, node)

    def insert_before(self, node: Node, node_to_insert: Node) -> None:
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node.prev
        node_to_insert.next = node
        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert

    def insert_after(self, node: Node, node_to_insert: Node) -> None:
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node
        node_to_insert.next = node.next
        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert
        node.next = node_to_insert

    def insert_at_position(self, position: int, node_to_insert: Node) -> None:
        if position == 1:
            self.set_head(node_to_insert)
            return
        node = self.head
        current_position: int = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1
        if node is not None:
            self.insert_before(node, node_to_insert)
        else:
            self.set_tail(node_to_insert)

    def remove_nodes_with_value(self, value: int) -> None:
        node = self.head
        while node:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    def remove(self, node: Node) -> None:
        if node == self.head:
            self.head = self.head.next if self.head else None
        if node == self.tail:
            self.tail = self.tail.prev if self.tail else None

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def contains_node_with_value(self, value: int) -> bool:
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
