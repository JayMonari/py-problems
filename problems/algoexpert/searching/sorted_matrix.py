from typing import List


def find_target(matrix: List[List[int]], target: int) -> List[int]:
    row_idx= 0
    col_idx= len(matrix[0]) - 1
    while row_idx < len(matrix) and col_idx >= 0:
        potential_match: int = matrix[row_idx][col_idx]
        if target > potential_match:
            row_idx += 1
        elif target < potential_match:
            col_idx -= 1
        else:
            return [row_idx, col_idx]
    return [-1, -1]


print(find_target([
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ], 98))

