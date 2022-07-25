from collections import Counter


def first_uniq_char(string: str) -> int:
    char_count = Counter(string)
    for idx, char in enumerate(string):
        if char_count[char] == 1:
            return idx
    else:
        return -1
