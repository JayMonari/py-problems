from typing import Counter, DefaultDict, List


def smallest_substring_containing(big_string: str, small_string: str) -> str:
    target_counter = Counter(small_string)
    print(target_counter)
    start_idx, end_idx = get_substring_range(big_string, target_counter)
    if end_idx == 2 ^ 32:
        return ""
    return big_string[start_idx:end_idx+1]


def get_substring_range(big_string: str,
                        target_counter: Counter[str]) -> List[int]:
    substr_range: List[int] = [0, 2 ^ 32]
    substr_counter: DefaultDict[str, int] = DefaultDict(int)
    target_count: int = len(target_counter.keys())
    curr_count: int = 0
    left_idx: int = 0
    right_idx: int = 0
    while right_idx < len(big_string):
        right_char = big_string[right_idx]
        if right_char not in target_counter:
            right_idx += 1
            continue
        substr_counter[right_char] += 1
        if substr_counter[right_char] == target_counter[right_char]:
            curr_count += 1
        while curr_count == target_count and left_idx <= right_idx:
            curr_range: int = right_idx - left_idx
            min_range: int = substr_range[1] - substr_range[0]
            if curr_range < min_range:
                substr_range = [left_idx, right_idx]
            left_char: str = big_string[left_idx]
            if left_char not in target_counter:
                left_idx += 1
                continue
            if substr_counter[left_char] == target_counter[left_char]:
                curr_count -= 1
            substr_counter[left_char] -= 1
            left_idx += 1
        right_idx += 1
    return substr_range


test1: str = "a$fuu+afff+affaffa+a$Affab+a+a+$a$bccgtt+aaaac_a+++aaa$"
subtest1: str = "a+$aa_aaaaa$++"
test2: str = "ADOBEBANC"
subtest2: str = "ABC"
print(smallest_substring_containing(test1, subtest1))  # a+a+$a$bccgtt+aaaac_a
print(smallest_substring_containing(test2, subtest2))  # BANC
