from typing import List


def search_for_range(nums: List[int], target: int) -> List[int]:
    final_range = [-1, -1]
    find_range(nums, target, 0, len(nums) - 1, final_range, True)
    find_range(nums, target, 0, len(nums) - 1, final_range, False)
    return final_range


def find_range(nums: List[int], target: int, left_idx: int,
               right_idx: int, final_range: List[int], go_left: bool) -> None:
    while left_idx <= right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2
        potential_match = nums[mid_idx]
        if target < potential_match:
            right_idx = mid_idx - 1
        elif target > potential_match:
            left_idx = mid_idx + 1
        if target != potential_match:
            continue

        if go_left:
            if mid_idx == 0 or nums[mid_idx - 1] != target:
                final_range[0] = mid_idx
                return
            else:
                right_idx = mid_idx - 1
        else:
            if mid_idx == len(nums) - 1 or nums[mid_idx + 1] != target:
                final_range[1] = mid_idx
                return
            else:
                left_idx = mid_idx + 1


test, target = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 45, 45, 45], 45
print(search_for_range(test, target))  # [4, 12]
