from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    new_len = 0
    for idx in range(1, len(nums)):
        if nums[new_len] == nums[idx]:
            continue
        new_len += 1
        nums[new_len] = nums[idx]
    return new_len + 1
