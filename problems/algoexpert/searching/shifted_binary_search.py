from typing import List


def shifted_binary_search(nums: List[int], target: int) -> int:
    left_idx = 0
    right_idx = len(nums) - 1
    while left_idx <= right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2
        potential_match = nums[mid_idx]
        left_bound = nums[left_idx]
        right_bound = nums[right_idx]
        if target == potential_match:
            return mid_idx
        elif left_bound <= potential_match:
            if target >= left_bound and target < potential_match:
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1
        else:
            if target <= right_bound and target > potential_match:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
    return -1


print(shifted_binary_search([33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 354))
print(shifted_binary_search([33, 45, 45, 62, 72, 72, 73, 355, 0, 2, 22], 355))
