from typing import Dict, List


def multi_string_search(string: str, words: List[str]) -> List[bool]:
    trie = Trie(words)
    contained_strings: Dict[str, bool] = {}
    for i in range(len(string)):
        node = trie.root
        for letter in string[i:]:
            if letter not in node:
                break

            node = node[letter]
            if trie.end_symbol in node:
                contained_strings[node[trie.end_symbol]] = True
    return [string in contained_strings for string in words]


class Trie:
    def __init__(self, words: List[str] = None):
        self.root = {}
        self.end_symbol = "#"
        if not words:
            return
        for w in words:
            self.insert(w)

    def insert(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = string


best = "ndbajwhfawkjljkfaopwdlaawjk dawkj awjkawkfjhkawk ahjwkjad jadfljawd"
sest = ["abc", "akwbc", "awbc", "abafac", "ajjfbc", "abac", "jadfl"]
best1 = "this is a big string"
sest1 = ["this", "yo", "is", "a", "bigger", "string", "sappa"]
print(multi_string_search(best1, sest1))
