from typing import List


ITEMS = [
    "the house that Jack built.",
    "the malt",
    "the rat",
    "the cat",
    "the dog",
    "the cow with the crumpled horn",
    "the maiden all forlorn",
    "the man all tattered and torn",
    "the priest all shaven and shorn",
    "the rooster that crowed in the morn",
    "the farmer sowing his corn",
    "the horse and the hound and the horn",
]

ACTIONS = [
    "lay in",
    "ate",
    "killed",
    "worried",
    "tossed",
    "milked",
    "kissed",
    "married",
    "woke",
    "kept",
    "belonged to",
    "",
]


def recite(start: int, end: int) -> List[str]:
    return [verse(n) for n in range(start, end+1)]


def verse(n: int) -> str:
    v = [f"This is {ITEMS[n-1]}"]
    for n in range(n - 2, -1, -1):
        v.append(f" that {ACTIONS[n]} {ITEMS[n]}")
    return "".join(v)
