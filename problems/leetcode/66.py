from typing import List


def plus_one(digits: List[int]) -> List[int]:
    remainder = False
    for idx in reversed(range(len(digits))):
        digits[idx] += 1
        if digits[idx] != 10:
            remainder = False
            break

        remainder = True
        digits[idx] = 0
    if remainder:
        digits.insert(0, 1)
    return digits
