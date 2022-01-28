from typing import Dict


def its_in_the_name(word: str) -> str:
    char_indices: Dict[str, int] = {}
    max_range = [0, 1]
    anchor_idx = 0
    for idx, char in enumerate(word):
        if char in char_indices:
            anchor_idx = max(anchor_idx, char_indices[char] + 1)
        [left_idx, right_idx] = max_range
        max_len = right_idx - left_idx
        curr_len = idx - anchor_idx + 1
        if max_len < curr_len:
            max_range = [anchor_idx, idx + 1]
        char_indices[char] = idx

    [left_idx, right_idx] = max_range
    return word[left_idx:right_idx]


test = 'brownchickenbrowncow'
print(its_in_the_name(test))
