from typing import List


def primes(limit: int) -> List[int]:
    is_prime = [True for _ in range(limit+1)]
    p = 2
    while (p * p <= limit):
        if (is_prime[p]):
            for fac in range(p**2, limit + 1, p):
                is_prime[fac] = False
        p += 1

    is_prime[0] = False
    is_prime[1] = False
    return [n for n in range(limit+1) if is_prime[n]]
