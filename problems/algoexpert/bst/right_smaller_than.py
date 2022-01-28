from typing import List, Optional


class BinarySearchTree:
    def __init__(self, value: int, left: Optional["BinarySearchTree"] = None,
                 right: Optional["BinarySearchTree"] = None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.left_subtree_size = 0

    def insert(self, value: int, idx: int, result: List[int],
               num_smaller_at_insertion_time=0) -> None:
        if value < self.value:
            self.left_subtree_size += 1
            if self.left is None:
                self.left = BinarySearchTree(value)
                result[idx] = num_smaller_at_insertion_time
            else:
                self.left.insert(
                    value, idx, result, num_smaller_at_insertion_time)
        else:
            num_smaller_at_insertion_time += self.left_subtree_size
            if value > self.value:
                num_smaller_at_insertion_time += 1
            if self.right is None:
                self.right = BinarySearchTree(value)
                result[idx] = num_smaller_at_insertion_time
            else:
                self.right.insert(
                    value, idx, result, num_smaller_at_insertion_time)


def right_smaller_than(nums: List[int]) -> List[int]:
    if not len(nums):
        return []

    result = nums[:]
    end_idx = len(nums) - 1
    bst = BinarySearchTree(nums[end_idx])
    result[end_idx] = 0
    for i in reversed(range(len(nums) - 1)):
        bst.insert(nums[i], i, result)
    return result


nums = [8, 5, 11, -1, 3, 4, 2]
gg = [
    991,
    -731,
    -882,
    100,
    280,
    -43,
    432,
    771,
    -581,
    180,
    -382,
    -998,
    847,
    80,
    -220,
    680,
    769,
    -75,
    -817,
    366,
    956,
    749,
    471,
    228,
    -435,
    -269,
    652,
    -331,
    -387,
    -657,
    -255,
    382,
    -216,
    -6,
    -163,
    -681,
    980,
    913,
    -169,
    972,
    -523,
    354,
    747,
    805,
    382,
    -827,
    -796,
    372,
    753,
    519,
    906
]
