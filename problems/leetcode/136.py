from typing import Counter, List


def single_number(nums: List[int]) -> int:
    nums_counter = Counter(nums)
    return nums_counter.most_common()[-1][0]
