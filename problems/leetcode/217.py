def contains_duplicate(nums: list[int]) -> bool:
    nums.sort()
    for idx in range(1, len(nums)):
        if nums[idx - 1] == nums[idx]:
            return True
    return False


def contains_duplicate2(nums: list[int]) -> bool:
    duplicates: set[int] = set()
    for num in nums:
        if num in duplicates:
            return True
        duplicates.add(num)
    return False
