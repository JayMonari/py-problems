from enum import Enum
from typing import List


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


class Category(Enum):
    YACHT = 0
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    LITTLE_STRAIGHT = 9
    BIG_STRAIGHT = 10
    CHOICE = 11


def score(dice: List[int], category: int) -> int:
    dice.sort()
    if category == Category.YACHT.value:
        return 50 if dice.count(dice[0]) == 5 else 0
    elif category == Category.ONES.value:
        return dice.count(1) * 1
    elif category == Category.TWOS.value:
        return dice.count(2) * 2
    elif category == Category.THREES.value:
        return dice.count(3) * 3
    elif category == Category.FOURS.value:
        return dice.count(4) * 4
    elif category == Category.FIVES.value:
        return dice.count(5) * 5
    elif category == Category.SIXES.value:
        return dice.count(6) * 6
    elif category == Category.FULL_HOUSE.value:
        return (sum(dice)
                if dice.count(dice[1]) + dice.count(dice[-2]) == 5
                else 0)
    elif category == Category.FOUR_OF_A_KIND.value:
        return dice[1] * 4 if dice.count(dice[1]) >= 4 else 0
    elif category == Category.LITTLE_STRAIGHT.value:
        return 30 if sum(set(filter(lambda n: n != 6, dice))) == 15 else 0
    elif category == Category.BIG_STRAIGHT.value:
        return 30 if sum(set(filter(lambda n: n != 1, dice))) == 20 else 0
    elif category == Category.CHOICE.value:
        return sum(dice)

    return 0
