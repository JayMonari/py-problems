from typing import List


events = [
    "wink",
    "double blink",
    "close your eyes",
    "jump",
]


def commands(binrep: str) -> List[str]:
    bits: List[int] = [ord(x) - ord('0') for x in binrep[::-1]]
    cmds: List[str] = [events[i] for i, b in enumerate(bits[:-1]) if b]
    if bits[-1]:
        cmds.reverse()
    return cmds
