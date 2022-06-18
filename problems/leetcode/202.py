def is_happy(number: int) -> bool:
    seen: set[int] = set()
    while number not in seen:
        seen.add(number)
        number = sum([int(digit) ** 2 for digit in str(number)])
    return number == 1


def detect_cycle(n: int) -> int:
    square_sum = 0
    while n:
        n, remainder = divmod(n, 10)
        square_sum += remainder * remainder
    return square_sum


def is_happy2(number: int) -> bool:
    slow = detect_cycle(number)
    fast = detect_cycle(detect_cycle(number))
    while slow != fast:
        if fast == 1:
            break
        slow = detect_cycle(slow)
        fast = detect_cycle(detect_cycle(fast))
    return fast == 1
