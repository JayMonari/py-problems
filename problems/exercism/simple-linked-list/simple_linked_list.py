from typing import Any, Iterable, List, Optional


class Node:

    def __init__(self, value: Any) -> None:
        self._value = value
        self._next: Optional["Node"] = None

    def value(self) -> Any:
        return self._value

    def next(self) -> Optional["Node"]:
        return self._next


class LinkedList:

    def __init__(self, values: List[Any] = []) -> None:
        if values:
            self._head: Optional["Node"] = Node(values[0])
            self.len = 1
            for n in values[1:]:
                self.push(n)
        else:
            self._head = None
            self.len = 0

    def __iter__(self) -> Iterable:
        node = self._head
        while node:
            yield node.value()
            node = node._next

    def __len__(self) -> int:
        return self.len

    def head(self) -> Optional["Node"]:
        if self.len == 0:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value: Any) -> None:
        self.len += 1

        tmp = self._head
        self._head = Node(value)
        self._head._next = tmp

    def pop(self) -> int:
        if not self._head:
            raise EmptyListException("The list is empty.")

        self.len -= 1
        tmp = self._head
        self._head = self._head._next
        return tmp.value()

    def reversed(self):
        return LinkedList(values=list(self))


class EmptyListException(Exception):
    pass
