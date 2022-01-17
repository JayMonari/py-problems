from typing import List

INT32_MIN: int = -2**31
INT32_MAX: int = 2**31 - 1
NULL_MARKER: int = -1


def is_same_BST(nodes1: List[int], nodes2: List[int]) -> bool:
    return recursive_helper(nodes1, nodes2, 0, 0, INT32_MIN, INT32_MAX)


def recursive_helper(
        nodes1: List[int],
        nodes2: List[int],
        root_idx1: int,
        root_idx2: int,
        min_value: int,
        max_value: int) -> bool:
    if root_idx1 == NULL_MARKER or root_idx2 == NULL_MARKER:
        return root_idx1 == root_idx2
    if nodes1[root_idx1] != nodes2[root_idx2]:
        return False

    left_root1: int = get_smaller_index(nodes1, root_idx1, min_value)
    left_root2: int = get_smaller_index(nodes2, root_idx2, min_value)
    right_root1: int = get_bigger_index(nodes1, root_idx1, max_value)
    right_root2: int = get_bigger_index(nodes2, root_idx2, max_value)

    curr_value: int = nodes1[root_idx1]
    is_same_leftside: bool = recursive_helper(
        nodes1, nodes2, left_root1, left_root2, min_value, curr_value)
    is_same_rightside: bool = recursive_helper(
        nodes1, nodes2, right_root1, right_root2, curr_value, max_value)
    print(f"current value: {curr_value} min: {min_value} max: {max_value}")
    print(f"leftside: {is_same_leftside} rightside: {is_same_rightside}")
    return is_same_leftside and is_same_rightside


def get_smaller_index(nodes: List[int], curr_idx: int, min_value: int) -> int:
    for index in range(curr_idx + 1, len(nodes)):
        if nodes[index] < nodes[curr_idx] and nodes[index] >= min_value:
            return index
    else:
        return NULL_MARKER


def get_bigger_index(nodes: List[int], curr_idx: int, max_value: int) -> int:
    for index in range(curr_idx + 1, len(nodes)):
        if nodes[index] >= nodes[curr_idx] and nodes[index] < max_value:
            return index
    else:
        return NULL_MARKER


array1 = [10, 15, 8, 12, 94, 81, 5, 2, 10]
array2 = [10, 8, 5, 15, 2, 10, 12, 94, 81]

print(is_same_BST(array1, array2))  # should be False
