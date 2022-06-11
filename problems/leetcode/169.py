from collections import Counter


def get_majority_element(nums: list[int]) -> int:
    test = Counter(nums)
    return test.most_common(1)[0][0]


def get_majority_element2(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]
