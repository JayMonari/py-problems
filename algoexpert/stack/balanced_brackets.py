from typing import List


def are_balanced(pairs: str) -> bool:
    OPEN_PAIRS = "([{"
    CLOSE_PAIRS = "}])"
    MATCHING_PAIRS = {'}': '{', ']': '[', ')': '('}
    stack: List[str] = []
    for pair_part in pairs:
        if pair_part in OPEN_PAIRS:
            stack.append(pair_part)
        if pair_part not in CLOSE_PAIRS:
            continue
        if not len(stack):
            return False
        top_open_pair: str = stack.pop()
        if not top_open_pair == MATCHING_PAIRS[pair_part]:
            return False
    return len(stack) == 0


test = "(((((({{{{{[[[[[([a])]]]]]}}}}}))))))"
test2 = "((((({{{{{[[[[[([a])]]]]]}}}}}))))))"
test3 = "}}])"
print(are_balanced(test3), are_balanced(test2), are_balanced(test))
