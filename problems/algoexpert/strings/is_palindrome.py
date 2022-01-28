def is_palindrome(string: str) -> bool:
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def is_palindrome2(string: str, left_idx: int = 0) -> bool:
    right_idx = len(string) - 1 - left_idx
    if left_idx >= right_idx:
        return True
    if string[left_idx] != string[right_idx]:
        return False
    return is_palindrome2(string, left_idx + 1)


test = "abc1d1cba"
test2 = "abc1d1cba2"
print(
    is_palindrome(test), is_palindrome(test2),
    is_palindrome2(test), is_palindrome2(test2)
)
