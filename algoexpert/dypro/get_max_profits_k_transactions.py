import sys
from typing import List


def transaction_in_days(prices: List[int], k: int) -> List[int]:
    if not len(prices):
        return []

    even_profits: List[int] = [0 for _ in prices]
    odd_profits: List[int] = [0 for _ in prices]
    for i in range(1, k + 1):
        current_max = -sys.maxsize * 2
        if i % 2 == 1:
            curr_profits = odd_profits
            prev_profits = even_profits
        else:
            curr_profits = even_profits
            prev_profits = odd_profits
        for j in range(1, len(prices)):
            current_max = max(current_max, prev_profits[j - 1] - prices[j - 1])
            curr_profits[j] = max(curr_profits[j - 1], current_max + prices[j])
    return even_profits if k % 2 == 0 else odd_profits


test1 = [5, 11, 3, 50, 60, 90]
test2 = [1, 25, 12, 36, 14, 40]
test3 = [1, 100, 101, 200, 201, 300, 301, 400, 401, 500]
for t in (test1, test2, test3):
    print(transaction_in_days(t, 5))
