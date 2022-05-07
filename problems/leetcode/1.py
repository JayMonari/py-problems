from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen: Dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        else:
            seen[num] = idx
    else:
        return [-1, -1]
