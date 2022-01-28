def is_pangram(sentence: str) -> bool:
    sentence = sentence.lower()
    for c in range(ord('a'), ord('z') + 1):
        if sentence.count(chr(c)) == 0:
            return False
    return True
