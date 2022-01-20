from typing import List, Literal


class Trie:
    def __init__(self, words: List[str] = None):
        self.root = {}
        self.end_symbol: Literal['*'] = "*"
        if not words:
            return
        for word in words:
            self.add(word)

    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = word


def boggle_board(board: List[List[str]], words: List[str]) -> List[str]:
    trie = Trie(words)
    found_words: List[str] = []
    visited: List[List[bool]] = [[False for _ in row] for row in board]
    for row in range(len(board)):
        for col in range(len(board[row])):
            search_for_words_in(board, row, col, trie.root,
                                visited, found_words)
    return found_words


def search_for_words_in(
        board: List[List[str]],
        row: int,
        col: int,
        node,
        visited: List[List[bool]],
        found_words: List[str]) -> None:
    if visited[row][col]:
        return
    char = board[row][col]
    if char not in node:
        return

    visited[row][col] = True
    node = node[char]
    if "*" in node:
        found_words.append(node['*'])
    chars_around: List[List[int]] = get_chars_around(row, col, board)
    for row, col in chars_around:
        search_for_words_in(
            board, row, col, node, visited, found_words)
    visited[row][col] = False


def get_chars_around(
        row: int,
        col: int,
        board:  List[List[str]]) -> List[List[int]]:
    chars_around: List[List[int]] = []
    last_row: int = len(board) - 1
    last_col: int = len(board[0]) - 1
    if row > 0:
        chars_around.append([row - 1, col])
    if row < last_row:
        chars_around.append([row + 1, col])
    if col > 0:
        chars_around.append([row, col - 1])
    if col < last_col:
        chars_around.append([row, col + 1])
    if row > 0 and col > 0:
        chars_around.append([row - 1, col - 1])
    if row > 0 and col < last_col:
        chars_around.append([row - 1, col + 1])
    if row < last_row and col > 0:
        chars_around.append([row + 1, col - 1])
    if row < last_row and col < last_col:
        chars_around.append([row + 1, col + 1])
    return chars_around


test = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"]
]
strings = [
    "this",
    "is",
    "not",
    "a",
    "simple",
    "boggle",
    "board",
    "test",
    "REPEATED",
    "NOTRE-PEATED"
]
print(boggle_board(test, strings))
