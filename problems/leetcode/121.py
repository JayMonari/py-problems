from typing import List, Union


def find_max_profit(prices: List[int]) -> int:
    max_profit = 0
    min_price: Union[float, int] = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        curr_profit = price - int(min_price)
        max_profit = max(max_profit, curr_profit)
    return max_profit
