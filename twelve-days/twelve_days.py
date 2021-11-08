from typing import List

presents: List[str] = [
    "and a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,",
]

days: List[str] = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def build_verse(num: int) -> str:
    start = f"On the {days[num]} day of Christmas my true love gave to me:"
    if num == 0:
        return f"{start} {presents[num][4:]}"

    return f"{start} {' '.join([presents[i] for i in range(num, -1, -1)])}"


def recite(_from: int, to: int) -> List[str]:
    return [build_verse(n-1) for n in range(_from, to+1)]
