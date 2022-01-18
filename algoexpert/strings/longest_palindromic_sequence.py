from typing import List


def find_max_palindrome(word: str) -> str:
    if len(word) < 2:
        return word

    def get_range(x): return x[1] - x[0]
    max_range: List[int] = [0, 1]
    for idx in range(len(word)):
        odd_range: List[int] = get_palindrome_range(word, idx, idx)
        even_range: List[int] = get_palindrome_range(word, idx, idx + 1)
        best_range = max(odd_range, even_range, key=get_range)
        max_range = max(max_range, best_range, key=get_range)

    start_idx, end_idx = max_range
    return word[start_idx:end_idx]


def get_palindrome_range(word: str,
                         left_idx: int,
                         right_idx: int) -> List[int]:
    while left_idx >= 0 and right_idx < len(word):
        if word[left_idx] != word[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return [left_idx + 1, right_idx]


test1, test2 = "it's highnoon", "abaghgxyzzyxf"
print(find_max_palindrome(test1), find_max_palindrome(test2))
