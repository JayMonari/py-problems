from typing import List

OPEN_PAIRS = "([{"
CLOSE_PAIRS = "}])"
MATCHING_PAIRS = {"{": "}", "[": "]", "(": ")"}


def are_valid_pairs(pairs: str) -> bool:
    stack: List[str] = []
    for char in pairs:
        if char in OPEN_PAIRS:
            stack.append(char)
        if char not in CLOSE_PAIRS:
            continue

        if not len(stack):
            return False

        open_pair = stack.pop()
        if MATCHING_PAIRS[open_pair] != char:
            return False
    return len(stack) == 0
