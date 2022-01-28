from typing import List


CONV_DICT = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def roman(n: int) -> str:
    roman_str: List[str] = []
    for rm, num in CONV_DICT.items():
        while n >= num:
            roman_str.append(rm)
            n -= num
    return "".join(roman_str)
