from typing import List, Optional

from BinarySearchTree import BinarySearchTree


def in_order_traverse(root: Optional[BinarySearchTree],
                      nums: List[int]) -> List[int]:
    if root is not None:
        in_order_traverse(root.left, nums)
        nums.append(root.value)
        in_order_traverse(root.right, nums)
    return nums


def pre_order_traverse(root: Optional[BinarySearchTree],
                       nums: List[int]) -> List[int]:
    if root is not None:
        nums.append(root.value)
        pre_order_traverse(root.left, nums)
        pre_order_traverse(root.right, nums)
    return nums


def post_order_travese(root: Optional[BinarySearchTree],
                       nums: List[int]) -> List[int]:
    if root is not None:
        post_order_travese(root.left, nums)
        post_order_travese(root.right, nums)
        nums.append(root.value)
    return nums
