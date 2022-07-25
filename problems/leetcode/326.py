def is_power_of(power: int, num: int) -> bool:
    if num < 1:
        return False
    while (num % power == 0):
        num //= power
    return num == 1
