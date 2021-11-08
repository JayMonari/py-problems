from enum import Enum
from typing import List


"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Left for tests
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

class Category(Enum):
    SUBLIST = 1
    SUPERLIST = 2
    EQUAL = 3
    UNEQUAL = 4


def sublist(list_one: List[int], list_two: List[int]) -> int:
    str1 = ','.join(map(lambda n: str(n), list_one))
    str2 = ','.join(map(lambda n: str(n), list_two))
    if str2 == str1:
        return Category.EQUAL.value
    elif str1.find(str2) != -1:
        return Category.SUPERLIST.value
    elif str2.find(str1) != -1:
        return Category.SUBLIST.value

    return Category.UNEQUAL.value
