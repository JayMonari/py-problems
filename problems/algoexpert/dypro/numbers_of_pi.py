from typing import Dict, List, Set


def numbers_in_pi(pi: str, numbers: List[str]) -> float:
    nums_set = {n for n in numbers}
    min_spaces: float = get_min_spaces(pi, nums_set, {}, 0)
    return -1 if min_spaces == float("inf") else min_spaces


def get_min_spaces(pi: str, nums_set: Set[str],
                   cache: Dict[int, float], idx: int) -> float:
    if idx == len(pi):
        return -1
    elif idx in cache:
        return cache[idx]

    min_spaces = float("inf")
    for i in range(idx, len(pi)):
        if pi[idx:i+1] in nums_set:
            min_spaces_in_suffix = get_min_spaces(
                pi, nums_set, cache, i + 1)
            min_spaces = min(min_spaces, min_spaces_in_suffix + 1)
    cache[idx] = min_spaces
    return cache[idx]


test = ["3", "314", "49", "9001", "15926535897", "14", "93238462643383279",
        "9323", "8462643383279", "4", "793"]
n_test = ["3141", "1512", "159", "592", "59265", "793", "12412451",
          "8462643383279"]

print(numbers_in_pi("3141592653589793238462643383279", test))
