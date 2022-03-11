from typing import List


def build_pascal_triangle(rows: int) -> List[List[int]]:
    triangle = [[1]]
    for row_idx in range(1, rows):
        prev_row = triangle[row_idx - 1]
        row = [1]
        for col in range(1, len(prev_row)):
            row.append(prev_row[col - 1] + prev_row[col])
        row.append(1)
        triangle.append(row)
    return triangle
