def get_missing_num(nums: list[int]) -> int:
    missing_num: int = len(nums)
    for i in range(len(nums)):
        missing_num ^= i
        missing_num ^= nums[i]
    return missing_num


def get_missing_num2(nums: list[int]) -> int:
    nums.sort()
    if nums[0] != 0:
        return 0
    if nums[-1] != len(nums):
        return len(nums)

    for idx in range(1, len(nums)):
        expected: int = nums[idx - 1] + 1
        if nums[idx] == expected:
            continue
        return expected
    else:
        return -1


def get_missing_num3(nums: list[int]) -> int:
    nums_set: set[int] = set(nums)
    for num in range(len(nums) + 1):
        if num not in nums_set:
            return num
    else:
        return -1
