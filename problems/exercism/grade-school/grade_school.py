from typing import Dict, List


class School:
    def __init__(self) -> None:
        self.students: Dict[int, List[str]] = {}

    def add_student(self, name: str, grade: int) -> None:
        self.students.setdefault(grade, [])
        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self) -> List[str]:
        return [n for _, ns in sorted(self.students.items()) for n in ns]


    def grade(self, grade: int) -> List[str]:
        return [] if self.students.get(grade) == None else self.students[grade]
