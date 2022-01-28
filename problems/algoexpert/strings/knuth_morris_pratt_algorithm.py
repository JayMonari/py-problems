from typing import List


def make_pattern(word: str) -> List[int]:
    repeating_indices: List[int] = [-1 for _ in word]
    anchor_idx: int = 0
    lead_idx: int = 1
    while lead_idx < len(word):
        if word[lead_idx] == word[anchor_idx]:
            repeating_indices[lead_idx] = anchor_idx
            lead_idx += 1
            anchor_idx += 1
        elif anchor_idx > 0:
            anchor_idx = repeating_indices[anchor_idx - 1] + 1
        else:
            lead_idx += 1
    return repeating_indices


def matches_pattern(word: str, target: str, pattern: List[int]) -> bool:
    str_idx = 0
    substr_idx = 0
    while str_idx + len(target) - substr_idx <= len(word):
        if target[substr_idx] == word[str_idx]:
            if substr_idx == len(target) - 1:
                return True
            str_idx += 1
            substr_idx += 1
        elif substr_idx > 0:
            substr_idx = pattern[substr_idx - 1] + 1
        else:
            str_idx += 1
    return False


def kmp_algorithm(word: str, target: str) -> bool:
    indices_pattern: List[int] = make_pattern(target)
    return matches_pattern(word, target, indices_pattern)


test, subtest = "adafccfefbbbfeeccbcfd", "eccb"
print(kmp_algorithm(test, subtest))
