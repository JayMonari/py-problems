from typing import List


def decode(s: str) -> str:
    sb: List[str] = []
    i = 0
    while i < len(s):
        next_idx = i
        while next_idx < len(s) and '0' <= s[next_idx] <= '9':
            next_idx += 1
        try:
            count = int(s[i:next_idx])
        except ValueError:
            count = 1
        i = next_idx + 1 if next_idx != i else i + 1
        sb.append(count * s[next_idx])
    return "".join(sb)


def encode(s: str) -> str:
    sb: List[str] = []
    while len(s) > 0:
        ch = s[0]
        unstripped_len = len(s)
        s = s.lstrip(ch)
        ch_count = unstripped_len - len(s)
        if ch_count > 1:
            sb.append(str(ch_count))
        sb.append(ch)
    return "".join(sb)
