from typing import List


PAIRINGS = {
    '{': '}',
    '[': ']',
    '(': ')',
}


def is_paired(line: str) -> bool:
    open_pairs: List[str] = []
    def is_pair_part(p): return "([{}])".find(p) != -1
    def is_open_part(p): return "([{".find(p) != -1
    for pair_part in line:
        if not is_pair_part(pair_part):
            continue

        if is_open_part(pair_part):
            open_pairs.append(pair_part)
            continue

        if len(open_pairs) == 0:
            return False

        if PAIRINGS[open_pairs.pop()] != pair_part:
            return False

    return len(open_pairs) == 0
