def is_isogram(phrase: str) -> bool:
    phrase = phrase.lower()
    counts = {ch: phrase.count(ch) for ch in phrase if ch != ' ' and ch != '-'}
    return all(count == 1 for count in counts.values())
