def reverse_int32(int32: int) -> int:
    sign = [1, -1][int32 < 0]
    rst = sign * int(str(abs(int32))[::-1])
    return rst if -(2**31)-1 < rst < 2**31 else 0
