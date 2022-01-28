def steps(number: int) -> int:
    if number < 1:
        raise ValueError("Number must be greater than one.")

    total = 0
    while number != 1:
        total += 1
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1

    return total
