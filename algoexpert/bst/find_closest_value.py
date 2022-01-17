from typing import Optional


class TreeNode:
    def __init__(self) -> None:
        self.value = 0
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def get_closest_value(root: Optional[TreeNode], target: int) -> int:
    if root == None:
        return 0

    closest_value = root.value
    def get_closest_to(t, c, x): return max(abs(t - c), abs(t - x))
    while root:
        closest_value = get_closest_to(target, root.value, closest_value)
        if closest_value == target:
            break

        if target < root.value:
            root = root.left
        elif target > root.value:
            root = root.right
    return closest_value
