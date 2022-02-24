from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left_idx = 0
    right_idx = len(nums) - 1
    while left_idx <= right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2
        curr_val = nums[mid_idx]
        if curr_val == target:
            return mid_idx
        elif curr_val < target:
            left_idx = mid_idx - 1
        elif curr_val > target:
            right_idx = mid_idx + 1
    return -1
