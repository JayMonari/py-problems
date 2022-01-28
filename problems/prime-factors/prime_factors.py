from typing import List


def factors(n: int) -> List[int]:
    facs: List[int] = []
    f = 2
    while n > 1:
        if n % f == 0:
            n //= f
            facs.append(f)
        else:
            f += 1
    return facs
