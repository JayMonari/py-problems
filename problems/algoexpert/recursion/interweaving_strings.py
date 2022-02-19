from typing import List


def interwoven_strings(s1: str, s2: str, interwoven: str) -> bool:
    if len(interwoven) != len(s2) + len(s1):
        return False

    cache: List[List[bool]] = [
        [False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    return are_interwoven(s1, s2, interwoven, 0, 0, cache)


def are_interwoven(s1: str, s2: str, interwoven: str, i1: int, i2: int,
                   cache: List[List[bool]]) -> bool:
    if cache[i1][i2]:
        return cache[i1][i2]

    i3 = i1 + i2
    if i3 == len(interwoven):
        return True

    if i1 < len(s1) and s1[i1] == interwoven[i3]:
        cache[i1][i2] = are_interwoven(
            s1, s2, interwoven, i1 + 1, i2, cache)
        if cache[i1][i2]:
            return True

    if i2 < len(s2) and s2[i2] == interwoven[i3]:
        cache[i1][i2] = are_interwoven(
            s1, s2, interwoven, i1, i2 + 1, cache)
        return cache[i1][i2]

    cache[i1][i2] = False
    return cache[i1][i2]


print(interwoven_strings("aaaaaaaaa", "aaaaaaaaaaf", "aaaaaaaaaaaaaaaaaaaf"))
