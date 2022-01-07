from typing import List

Knapsack = List[List[int]]


def populate_knapsack(items: Knapsack, max_weight: int) -> Knapsack:
    knapsack = [[0 for _ in range(max_weight + 1)]
                for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        value, weight = items[i - 1]
        for w in range(max_weight + 1):
            if weight > w:
                knapsack[i][w] = knapsack[i - 1][w]
            else:
                knapsack[i][w] = max(
                    knapsack[i - 1][w], knapsack[i - 1][w - weight] + value)
    return knapsack


def get_item_indices(knapsack: Knapsack, items: Knapsack) -> List[int]:
    sequence: List[int] = []
    curr_weight = len(knapsack[0]) - 1
    for i in reversed(range(1, len(knapsack))):
        if knapsack[i][curr_weight] == knapsack[i - 1][curr_weight]:
            continue

        sequence.append(i - 1)
        curr_weight -= items[i - 1][1]
        if curr_weight == 0:
            break
    return list(reversed(sequence))


def knapsack_problem(items: Knapsack, max_weight: int) -> List[int]:
    knapsack: List[List[int]] = populate_knapsack(items, max_weight)
    return get_item_indices(knapsack, items)


test1 = [[1, 2], [4, 3], [5, 6], [6, 7]]
test2 = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [2400, 40]
]
test_weight1: int = 10
test_weight2: int = 300
print(knapsack_problem(test1, test_weight1))
print(knapsack_problem(test2, test_weight2))
