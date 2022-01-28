from typing import Optional


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.right: Optional[TreeNode] = None
        self.left: Optional[TreeNode] = None


def validate_BST(root: TreeNode) -> bool:
    return is_valid(root, -2 ** 31, 2 ** 31 - 1)


def is_valid(node: Optional[TreeNode], min_value: int, max_value: int) -> bool:
    if node is None:
        return True
    if node.value < min_value or node.value > max_value:
        return False

    is_valid_leftside = is_valid(node.left, min_value, node.value)
    is_valid_rightside = is_valid(node.right, min_value, node.value)
    return is_valid_leftside and is_valid_rightside
