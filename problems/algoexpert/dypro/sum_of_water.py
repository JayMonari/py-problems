from typing import List


def sum_of_water(nums: List[int]) -> int:
    maxes = [0 for _ in nums]
    left_max = 0
    for i in range(len(nums)):
        maxes[i] = left_max
        left_max = max(left_max, nums[i])
    right_max = 0
    for i in reversed(range(len(nums))):
        min_height = min(right_max, maxes[i])
        if nums[i] < min_height:
            maxes[i] = min_height - nums[i]
        else:
            maxes[i] = 0
        right_max = max(right_max, nums[i])
    return sum(maxes)


print(sum_of_water([0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 100]))
