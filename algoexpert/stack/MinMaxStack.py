from typing import Dict, List


class MinMaxStack:
    def __init__(self) -> None:
        self.stack: List[Dict[str, int]] = []

    def peek(self) -> int:
        return self.stack[-1]["value"]

    def pop(self) -> int:
        return self.stack.pop()["value"]

    def push(self, value: int) -> None:
        if not len(self.stack):
            self.stack.append({"value": value, "min": value, "max": value})
            return
        next_min: int = min(value, self.stack[-1]["min"])
        next_max: int = max(value, self.stack[-1]["max"])
        self.stack.append({"value": value, "min": next_min, "max": next_max})

    def get_min(self) -> int:
        return self.stack[-1]["min"]

    def get_max(self) -> int:
        return self.stack[-1]["max"]


mms = MinMaxStack()
mms.push(5)
mms.push(4)
mms.push(8)
mms.push(33)
mms.push(324)
mms.push(34)
mms.push(42)
print(f"peek {mms.peek()}")
print(f"get_min {mms.get_min()}")
print(f"get_max {mms.get_max()}")
mms.pop()
print(f"peek {mms.peek()}")
