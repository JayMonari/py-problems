from typing import List


def get_max_ways_make_change(amount: int, coins: List[int]) -> int:
    max_ways = [0 for _ in range(amount + 1)]
    max_ways[0] = 1
    for coin_val in coins:
        for amt in range(amount + 1):
            if coin_val <= amt:
                max_ways[amt] += max_ways[amt - coin_val]
    return max_ways[-1]


n, denoms = 7, [1, 2, 3, 4, 7]
print(get_max_ways_make_change(n, denoms))  # 12
