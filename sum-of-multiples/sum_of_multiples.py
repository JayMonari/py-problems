from typing import List, Set


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    return sum(get_multiples(limit, multiples))


def get_multiples(limit: int, nums: List[int]) -> Set[int]:
    muls = set()
    for num in nums:
        if num == 0:
            continue
        for m in range(num, limit, num):
            muls.add(m)
    return muls
