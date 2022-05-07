from typing import List


def longest_common_prefix(words: List[str]) -> str:
    """Horizontal scanning"""
    prefix = words[0]
    for i in range(1, len(words)):
        while words[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def longest_common_prefix2(words: List[str]) -> str:
    """Vertical scanning"""
    for i in range(len(words[0])):
        char: str = words[0][i]
        for j in range(len(words)):
            if i == len(words[j]) or words[j][i] != char:
                return words[0][:i]
    return words[0]


def find_common_prefix(left: str, right: str) -> str:
    """DnC Divide & Conquer"""
    min_len: int = min(len(left), len(right))
    for idx in range(min_len):
        if left[idx] != right[idx]:
            return left[:idx]
    return left[:min_len]


def dnc(words: List[str], start_idx: int, end_idx: int) -> str:
    if start_idx == end_idx:
        return words[start_idx]
    mid_idx = start_idx + (end_idx - start_idx) // 2
    lcp_left = dnc(words, 0, mid_idx)
    lcp_right = dnc(words, mid_idx + 1, end_idx)
    return find_common_prefix(lcp_left, lcp_right)


def longest_common_prefix3(words: List[str]) -> str:
    return dnc(words, 0, len(words) - 1)


def is_common_prefix(words: List[str], length: int) -> bool:
    """Binary Search"""
    word: str = words[0][:length]
    for next_word in words[1:]:
        if not next_word.startswith(word):
            return False
    return True


def longest_common_prefix4(words: List[str]) -> str:
    min_len = min([len(w) for w in words])
    left_idx = 1
    right_idx = min_len
    while left_idx <= right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2
        if is_common_prefix(words, mid_idx):
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
    lcp_idx = left_idx + (right_idx - left_idx) // 2
    return words[0][:lcp_idx]
