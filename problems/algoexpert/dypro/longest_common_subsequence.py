from typing import List


def longest_common_subsequence(s1: str, s2: str) -> List[str]:
    lengths: List[List[int]] = [
        [0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
    return build_sequence(lengths, s1)


def build_sequence(lengths: List[List[int]], s: str) -> List[str]:
    sequence: List[str] = []
    i = len(lengths) - 1
    j = len(lengths[0]) - 1
    while i != 0 and j != 0:
        if lengths[i][j] == lengths[i - 1][j]:
            i -= 1
        elif lengths[i][j] == lengths[i][j - 1]:
            j -= 1
        else:
            sequence.append(s[j - 1])
            j -= 1
            i -= 1
    return list(reversed(sequence))


s1, s2 = "checkinbrow", "chickenbraw"

longest_common_subsequence(s1, s2)
