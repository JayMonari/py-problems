def reverse_bits(uint32: int) -> int:
    reversed_uint32 = 0
    mask = 0x01
    for _ in range(32):
        reversed_uint32 <<= 1
        least_significant_bit = uint32 & mask
        reversed_uint32 |= least_significant_bit
        uint32 >>= 1
    return reversed_uint32


def reverse_bits2(uint32: int) -> int:
    uint32 = (uint32 >> 16) | (uint32 << 16)
    uint32 = ((uint32 & 0xff00ff00) >> 8) | ((uint32 & 0x00ff00ff) << 8)
    uint32 = ((uint32 & 0xf0f0f0f0) >> 4) | ((uint32 & 0x0f0f0f0f) << 4)
    uint32 = ((uint32 & 0xcccccccc) >> 2) | ((uint32 & 0x33333333) << 2)
    uint32 = ((uint32 & 0xaaaaaaaa) >> 1) | ((uint32 & 0x55555555) << 1)
    return uint32
