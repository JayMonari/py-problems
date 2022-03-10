from typing import List, Optional

from .data_structures.TreeNode import TreeNode


def helper(nums: List[int], start: int, end: int) -> Optional[TreeNode]:
    if start > end:
        return None

    mid_idx = start + (end - start) // 2
    root = TreeNode(nums[mid_idx])
    root.left = helper(nums, start, mid_idx - 1)
    root.right = helper(nums, mid_idx + 1, end)
    return root


def sorted_list_to_BST(nums: List[int]) -> Optional[TreeNode]:
    return helper(nums, 0, len(nums) - 1)
