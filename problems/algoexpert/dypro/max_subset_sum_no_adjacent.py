from typing import List


def max_subset_sum_no_adjacent(nums: List[int]) -> int:
    if not len(nums):
        return 0
    elif len(nums) == 1:
        return nums[0]
    first = max(nums[0], nums[1])
    second = nums[0]
    for n in nums[2:]:
        current = max(first, second + n)
        second = first
        first = current
    return first


print(max_subset_sum_no_adjacent([44, 33, 99]))
print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
print(max_subset_sum_no_adjacent([30, 45, 50, 55, 100, 120]))
