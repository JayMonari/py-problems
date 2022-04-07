from typing import Dict

ROMAN_VALUES: Dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                                "D": 500, "M": 1000}


def roman_to_int(roman_num: str) -> int:
    result = 0
    for idx in range(1, len(roman_num)):
        prev, curr = roman_num[idx - 1], roman_num[idx]
        if ROMAN_VALUES[prev] < ROMAN_VALUES[curr]:
            result -= ROMAN_VALUES[prev]
        else:
            result += ROMAN_VALUES[prev]
    result += ROMAN_VALUES[roman_num[-1]]
    return result
