from typing import List


class Matrix:
    def __init__(self, values: str):
        self.rows = []
        self.cols = []
        self.__create_matrix(values)

    def row(self, index: int) -> List[int]:
        return self.rows[index-1]

    def column(self, index: int) -> List[int]:
        return self.cols[index-1]

    def __create_matrix(self, values: str) -> None:
        # Create rows
        for strrow in values.split('\n'):
            self.rows.append(list(map(lambda s: int(s), strrow.split(' '))))
        # Create columns
        self.cols = [[] for _ in range(len(self.rows) + 1)]
        for row in self.rows:
            col_idx = 0
            while col_idx < len(self.rows[0]):
                self.cols[col_idx].append(row[col_idx])
                col_idx += 1
