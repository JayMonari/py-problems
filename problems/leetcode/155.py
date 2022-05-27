MinVal = tuple[int, int]


class MinStack:
    def __init__(self) -> None:
        self.stack: list[MinVal] = []

    def push(self, val: int) -> None:
        if not len(self.stack):
            self.stack.append((val, val))
            return
        self.stack.append((min(val, self.stack[-1][0]), val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
