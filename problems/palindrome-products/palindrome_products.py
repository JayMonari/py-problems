from typing import List, Optional, Tuple


ValueFactorPair = Tuple[Optional[int], List[Tuple[int, int]]]


def palindrome(_min: int, _max: int, smallest: bool = True) -> ValueFactorPair:
    if _min > _max:
        raise ValueError("min must be smaller than max")
    args = (_min**2, _max**2 + 1) if smallest else (_max**2, _min**2 - 1, -1)
    for r in range(*args):
        s = str(r)
        if s == s[::-1] and any(_min <= r//j <= _max
                                for j in range(_min, _max + 1) if r % j == 0):
            return r, list((i, r//i) for i in range(_min, _max + 1)
                           if r % i == 0 and _min <= i <= r//i <= _max)
    else:
        return None, []


def largest(min_factor: int, max_factor: int) -> ValueFactorPair:
    return palindrome(min_factor, max_factor, smallest=False)


def smallest(min_factor: int, max_factor: int) -> ValueFactorPair:
    return palindrome(min_factor, max_factor)
