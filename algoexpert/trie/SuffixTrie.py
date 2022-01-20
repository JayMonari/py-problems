from typing import Any, Dict


class SuffixTrie:
    def __init__(self, string: str) -> None:
        self.root: Dict[str, Dict[str, Any]] = {}
        self.end_symbol = "#"
        self.populate_trie(string)

    def populate_trie(self, string: str) -> None:
        for idx in range(len(string)):
            trie_node: Dict[str, Dict[str, Any]] = self.root
            for char in string[idx:]:
                if char not in trie_node:
                    trie_node[char] = {}
                trie_node = trie_node[char]
            trie_node[self.end_symbol] = {}

    def contains(self, string: str) -> bool:
        trie_node = self.root
        for char in string:
            if char not in trie_node:
                return False
            trie_node = trie_node[char]
        return self.end_symbol in trie_node


test = SuffixTrie("ThisIsATest")
print(test.root, test.contains("est"))
