from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    word = word.lower()
    target = sorted(word)
    return [c for c in candidates
            if sorted(c.lower()) == target and c.lower() != word]
