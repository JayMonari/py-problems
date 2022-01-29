from typing import List, Optional


def min_jumps(nums: List[int]) -> float:
    jumps: List[float] = [float("inf") for _ in nums]
    jumps[0] = 0
    for i in range(1, len(nums)):
        for j, jump_amount in enumerate(nums[:i]):
            if jump_amount >= i - j:
                jumps[i] = min(jumps[j] + 1, jumps[i])
    return jumps[-1]


def cheeky(nums):
    if len(nums) == 1:
        return 0
    jumps = 0
    max_reach = nums[0]
    steps = nums[0]
    for i, jump_amount in enumerate(nums[1:-1], start=1):
        max_reach = max(max_reach, i + jump_amount)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i
    return jumps + 1


print(cheeky([3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]))
print(cheeky([2, 1, 2, 3, 1, 1, 1]))
print(min_jumps([3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]))
print(min_jumps([2, 1, 2, 3, 1, 1, 1]))
