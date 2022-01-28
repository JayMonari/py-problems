from typing import List, Optional


class TreeNode:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def make_min_height_bst(sorted_list: List[int]) -> Optional[TreeNode]:
    return construct(sorted_list, 0, len(sorted_list) - 1)


def construct(
        sorted_list: List[int],
        start_idx: int,
        end_idx: int) -> Optional[TreeNode]:
    if start_idx > end_idx:
        return None

    mid_idx = start_idx + (end_idx - start_idx) // 2
    root = TreeNode(sorted_list[mid_idx])
    root.left = construct(sorted_list, start_idx, mid_idx - 1)
    root.right = construct(sorted_list, mid_idx + 1, end_idx)
    return root
