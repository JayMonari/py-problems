from typing import List


def encrypt_with_ceasar_cipher(phrase: str, key: int) -> str:
    CODEPOINT_A = 97
    CODEPOINT_Z = 122
    encrypted_phrase: List[str] = []
    limitedKey = key % 26
    for char in phrase:
        new_codepoint = ord(char) + limitedKey
        if new_codepoint > CODEPOINT_Z:
            new_codepoint = (CODEPOINT_A - 1) + (new_codepoint % CODEPOINT_Z)
        encrypted_phrase.append(chr(new_codepoint))
    return "".join(encrypted_phrase)


test: str = "axyz"
print(encrypt_with_ceasar_cipher(test, 2))
