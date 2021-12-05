from typing import Any, Iterable


class CustomSet:
    def __init__(self, _elements: Iterable[Any] = []):
        self._elements = []
        for e in _elements:
            self.add(e)

    def isempty(self) -> bool:
        return len(self._elements) == 0

    def __contains__(self, element: Any) -> bool:
        return element in self._elements

    def issubset(self, other: "CustomSet") -> bool:
        return all(e in other for e in self._elements)

    def isdisjoint(self, other: "CustomSet") -> bool:
        return self.intersection(other).isempty()

    def __eq__(self, other: "CustomSet") -> bool:
        return len(self._elements) == len(other._elements) \
            and self.issubset(other)

    def add(self, element: Any) -> None:
        if element not in self._elements:
            self._elements.append(element)

    def intersection(self, other: "CustomSet") -> "CustomSet":
        return CustomSet(e for e in self._elements if e in other)

    def __sub__(self, other: "CustomSet") -> "CustomSet":
        return CustomSet(e for e in self._elements if e not in other)

    def __add__(self, other: "CustomSet") -> "CustomSet":
        return CustomSet(self._elements + other._elements)
