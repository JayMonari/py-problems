import re
from typing import DefaultDict


def count_words(sentence: str) -> DefaultDict[str, int]:
    counter = DefaultDict(int)
    def is_word(w): return w != ''
    for word in filter(is_word, re.split("[^0-9a-z']", sentence.lower())):
        counter[word.strip("'")] += 1

    return counter
