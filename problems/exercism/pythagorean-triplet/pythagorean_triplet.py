import math
from typing import List


# a**2 + b**2 = c**2
# a + b + c = N <->
# a**2 + b**2 = c**2
# a + b = N - c
# Solving system of equations for a and b
# D = sqrt(c**2 - N**2 + 2*N*c)
# a = (N - c - D)/2
# b = (N - c + D)/2
# D is real for c > N * (sqrt(2) - 1)
# And c < N/2 from the problem statement
def triplets_with_sum(number: int) -> List[List[int]]:
    N = float(number)
    triplets: List[List[int]] = []
    for c in range(int(N/2)-1, int((math.sqrt(2)-1)*N), -1):
        D = math.sqrt(c**2 - N**2 + 2*N*c)
        if D == int(D):
            triplets.append([int((N-c-D)/2), int((N-c+D)/2), c])
    return triplets
