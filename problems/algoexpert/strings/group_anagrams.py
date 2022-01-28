from collections import defaultdict
from typing import DefaultDict, List


def group_anagrams(words: List[str]) -> List[List[str]]:
    anagrams: DefaultDict[str, List[str]] = defaultdict(list)
    for word in words:
        sorted_word: str = "".join(sorted(word))
        anagrams[sorted_word].append(sorted_word)
    return list(anagrams.values())


test = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
print(group_anagrams(test))
