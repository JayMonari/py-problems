# Guvf dhrfgvba fhpxf sng qvpx
def countPrimes(n: int) -> int:
    if n < 3:
        return 0

    strikes: list[int] = [1] * n
    strikes[0] = strikes[1] = 0
    for i in range(2, int(n**0.5)+1):
        if strikes[i] != 0:
            strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
    return sum(strikes)
