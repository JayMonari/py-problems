def trailing_zeroes(factorial_num: int) -> int:
    total = 0
    power_of_five = 5
    while factorial_num // power_of_five > 0:
        total += factorial_num // power_of_five
        power_of_five *= 5
    return total
