def aliquot_sum(n: int) -> int:
    return sum([factor for factor in range(1, n//2+1) if n % factor == 0])


def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError(
            "Classification is only possible for positive integers.")

    sum = aliquot_sum(number)
    if sum < number:
        return "deficient"
    elif sum > number:
        return "abundant"
    return "perfect"
