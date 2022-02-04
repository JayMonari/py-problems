from typing import List, Tuple


RIVER = 1
Coordinate = Tuple[int, int]


def find_river_lengths(chart: List[List[int]]) -> List[int]:
    lengths: List[int] = []
    visited: List[List[bool]] = [[False for _ in row] for row in chart]
    for row in range(len(chart)):
        for col in range(len(chart[0])):
            if visited[row][col]:
                continue
            get_river_len(row, col, chart, visited, lengths)
    return lengths


def get_river_len(row: int,
                  col: int,
                  chart: List[List[int]],
                  visited: List[List[bool]],
                  lengths: List[int]) -> None:
    river_len = 0
    not_visited = [(row, col)]
    while len(not_visited) != 0:
        row, col = not_visited.pop()
        if visited[row][col]:
            continue
        visited[row][col] = True
        if not chart[row][col] == RIVER:
            continue
        river_len += 1
        not_visited.extend(get_nearby_values(row, col, chart, visited))
    if river_len > 0:
        lengths.append(river_len)


def get_nearby_values(row: int,
                      col: int,
                      chart: List[List[int]],
                      visited: List[List[bool]]) -> List[Coordinate]:
    adj_pos: List[Coordinate] = []
    if row > 0 and not visited[row - 1][col]:
        adj_pos.append((row - 1, col))
    if row < len(chart) - 1 and not visited[row + 1][col]:
        adj_pos.append((row + 1, col))
    if col > 0 and not visited[row][col - 1]:
        adj_pos.append((row, col - 1))
    if col < len(chart[0]) - 1 and not visited[row][col + 1]:
        adj_pos.append((row, col + 1))
    return adj_pos


test = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]
print(find_river_lengths(test))
