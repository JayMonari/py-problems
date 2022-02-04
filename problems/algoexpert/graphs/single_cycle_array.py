from typing import List


def can_one_cycle_list(nums: List[int]) -> bool:
    visit_amount = 0
    current_idx = 0
    while visit_amount < len(nums):
        if visit_amount > 0 and current_idx == 0:
            return False
        visit_amount += 1
        current_idx = get_next_idx(current_idx, nums)
    return current_idx == 0


def get_next_idx(i: int, nums: List[int]) -> int:
    jump = nums[i]
    next_idx = (i + jump) % len(nums)
    return next_idx


print(can_one_cycle_list(
    [3, 5, 6, -5, -2, -5, -28, -2, -1, 2, -6, 1, 1, 2, -5, 2]
))
