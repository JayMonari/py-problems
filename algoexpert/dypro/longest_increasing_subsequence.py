# O(nlogn) T | O(n) S

from typing import List, Optional


def longest_increasing_subsequence(nums: List[int]) -> List[int]:
    max_length = 0
    sequences: List[Optional[int]] = [None for _ in nums]
    idxs: List[Optional[int]] = [None for _ in range(len(nums)+1)]
    for i, num in enumerate(nums):
        new_length = binary_search(1, max_length, nums, idxs, num)
        sequences[i] = idxs[new_length-1]
        idxs[new_length] = i
        max_length = max(max_length, new_length)
    return build_sequence(nums, sequences, idxs[max_length])


def binary_search(start_idx: int, end_idx: int, nums: List[int],
                  idxs: List[Optional[int]], num: int) -> int:
    if start_idx > end_idx:
        return start_idx

    mid_idx = (start_idx + end_idx) // 2
    if nums[idxs[mid_idx]] < num:
        start_idx = mid_idx + 1
    elif nums[idxs[mid_idx]] > num:
        end_idx = mid_idx - 1
    return binary_search(start_idx, end_idx, nums, idxs, num)


def build_sequence(nums: List[int], sequences: List[Optional[int]],
                   current_idx: Optional[int]) -> List[int]:
    sequence: List[int] = []
    while current_idx is not None:
        sequence.append(nums[current_idx])
        current_idx = sequences[current_idx]
    return list(reversed(sequence))


test = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(longest_increasing_subsequence(test))
