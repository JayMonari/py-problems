from typing import Dict, List


class Garden:
    def __init__(self, diagram: str,
                 students: List[str] = [
                     "Alice",
                     "Bob",
                     "Charlie",
                     "David",
                     "Eve",
                     "Fred",
                     "Ginny",
                     "Harriet",
                     "Ileana",
                     "Joseph",
                     "Kincaid",
                     "Larry"]) -> None:
        self.__plant_names = {
            'R': "Radishes",
            'G': "Grass",
            'C': "Clover",
            'V': "Violets"
        }
        self.students = sorted(students)
        self.assigned_plants = self.__assign_plants(diagram)

    def __assign_plants(self, diagram: str) -> Dict[str, List[str]]:
        assigned: Dict[str, List[str]] = {}

        [row1, row2] = diagram.split('\n')
        for i in range(0, min(len(row1), len(self.students)), 1):
            student_plants = [row1[(i*2):(i*2)+2], row2[(i*2):(i*2)+2]]
            assigned[self.students[i]] = \
                self.__give_full_name(''.join(student_plants))
        return assigned

    def __give_full_name(self, row: str) -> List[str]:
        return [self.__plant_names[p] for p in row]

    def plants(self, name: str) -> List[str]:
        return self.assigned_plants[name]
