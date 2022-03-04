def is_armstrong_number(number: int) -> bool:
    digits = str(number)
    return sum(int(d)**len(digits) for d in digits) == number
