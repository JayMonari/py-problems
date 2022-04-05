from typing import List


def get_max_profit(prices: List[int]) -> int:
    max_profit = 0
    for prev_day_price, curr_day_price in zip(prices, prices[1:]):
        if curr_day_price > prev_day_price:
            max_profit += curr_day_price - prev_day_price
    return max_profit
