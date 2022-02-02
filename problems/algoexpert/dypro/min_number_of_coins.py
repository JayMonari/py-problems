from typing import List


def min_num_of_coins(n: int, coin_values: List[int]) -> float:
    smallest_ways = [float("inf") for _ in range(n + 1)]
    smallest_ways[0] = 0
    for val in coin_values:
        for amt in range(len(smallest_ways)):
            if val <= amt:
                smallest_ways[amt] = min(
                    smallest_ways[amt], smallest_ways[amt - val] + 1)
    return smallest_ways[-1] if smallest_ways[-1] != float("inf") else -1


print(min_num_of_coins(13, [2, 4]))
