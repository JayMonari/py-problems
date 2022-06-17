def hamming_weight(n: int) -> int:
    count_of_1_bits = 0
    while (n):
        count_of_1_bits += n & 1
        n >>= 1
    return count_of_1_bits
