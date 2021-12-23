from itertools import cycle
import secrets
import string
from typing import Optional


class Cipher:
    START = ord('a')
    ALPHA_LEN = ord('z') - ord('a') + 1

    def __init__(self, key: Optional[str] = None) -> None:
        if not key:
            key = "".join(secrets.choice(string.ascii_lowercase)
                          for _ in range(100))
        self.key: str = key

    def encode(self, text: str) -> str:
        return "".join(string.ascii_lowercase[self._rotate(ord(ch1), ord(ch2))]
                       for ch1, ch2 in zip(text, cycle(self.key)))

    def decode(self, text: str) -> str:
        return "".join(string.ascii_lowercase[self._rotate(ord(ch1), ord(ch2),
                                                           dec=True)]
                       for ch1, ch2 in zip(text, cycle(self.key)))

    def _rotate(self, ord1: int, ord2: int, dec: bool = False) -> int:
        if dec:
            return (ord1 % self.START - ord2 % self.START) % self.ALPHA_LEN
        return (ord1 % self.START + ord2 % self.START) % self.ALPHA_LEN
