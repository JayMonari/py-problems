from typing import Callable


def title_to_int(column_title: str) -> int:
    number = 0
    convert_to_ord: Callable[[str], int] = lambda l: ord(l) - ord('A') + 1
    for letter in column_title:
        number = number * 26 + convert_to_ord(letter)
    return number
