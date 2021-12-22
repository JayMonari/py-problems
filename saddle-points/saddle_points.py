from typing import Dict, List

SaddlePoint = Dict[str, int]
Matrix = List[List[int]]


def get_row_maxes(m: Matrix) -> List[int]:
    return [max([col for col in row]) for row in m]


def get_col_mins(m: Matrix) -> List[int]:
    columns: List[List[int]] = [[] for _ in range(len(m[0]))]
    for i in range(len(m[0])):
        for row in m:
            columns[i].append(row[i])
    return [min(c) for c in columns]


def saddle_points(matrix: Matrix) -> List[SaddlePoint]:
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    if not matrix:
        return []
    row_maxes = get_row_maxes(matrix)
    col_mins = get_col_mins(matrix)
    points: List[SaddlePoint] = []
    for ridx in range(len(matrix)):
        for cidx in range(len(matrix[0])):
            candidate = matrix[ridx][cidx]
            if candidate == row_maxes[ridx] and candidate == col_mins[cidx]:
                points.append({"row": ridx+1, "column": cidx+1})
    return points
