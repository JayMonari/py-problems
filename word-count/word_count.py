import re
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    counter: Dict[str, int] = {}
    is_word = lambda w: w != ''
    for word in filter(is_word, re.split("[^0-9a-z']", sentence.lower())):
        word = word.strip("'")
        counter[word] = counter.setdefault(word, 0) + 1
    return counter
