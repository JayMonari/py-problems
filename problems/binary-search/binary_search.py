from typing import List


def find(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (hi + lo) // 2
        cand = nums[mid]
        if cand < target:
            lo = mid + 1
        elif cand > target:
            hi = mid - 1
        else:
            return mid
    raise ValueError("value not in array")
