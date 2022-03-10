from collections import deque
from typing import Deque
from .data_structures.TreeNode import TreeNode


def is_mirrored(left: TreeNode, right: TreeNode) -> bool:
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val
            and is_mirrored(left.left, right.right)
            and is_mirrored(left.right, right.left))


def is_symmetric_rec(root: TreeNode) -> bool:
    return is_mirrored(root.left, root.right)


def is_symmetric_iter(root: TreeNode) -> bool:
    nodes: Deque[TreeNode] = deque([root, root])
    while len(nodes):
        left = nodes.popleft()
        right = nodes.popleft()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        nodes.extend([left.left, right.right, left.right, right.left])
    return True
