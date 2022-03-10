from .data_structures.TreeNode import TreeNode


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1
