from functools import reduce


def square(exponent: int) -> int:
    if exponent < 1:
        raise ValueError("Exponent must be greater than 0")
    if exponent > 64:
        raise ValueError("Exponent must be less than 64")
    return 2**(exponent - 1)


def total():
    value_each_day = [v for v in map(square, [n for n in range(1, 65)])]
    return reduce(lambda a, b: a+b, value_each_day)
