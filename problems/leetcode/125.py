def is_palindrome(string: str) -> bool:
    left = 0
    right = len(string) - 1
    while left < right:
        while not string[left].isalnum() and left < right:
            left += 1
        while not string[right].isalnum() and left < right:
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1
    return True
