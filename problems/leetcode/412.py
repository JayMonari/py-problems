def fizz_buzz(n: int) -> list[str]:
    result: list[str] = []
    def is_divisible_by(m: int, n: int) -> bool: return n % m == 0
    for number in range(1, n + 1):
        if is_divisible_by(3, number) and is_divisible_by(5, number):
            result.append("FizzBuzz")
        elif is_divisible_by(3, number):
            result.append("Fizz")
        elif is_divisible_by(5, number):
            result.append("Buzz")
        else:
            result.append(str(number))
    return result
