from typing import List, Optional, Tuple


SumAndSubsequence = Tuple[int, List[int]]


def max_sum_increasing_subsequence(nums: List[int]) -> SumAndSubsequence:
    """Docstrings are for nerdz 😜"""
    sequences: List[Optional[int]] = [None for _ in nums]
    sums = nums[:]
    max_sum_idx = 0
    for i, num1 in enumerate(nums[1:], start=1):
        for j, num2 in enumerate(nums[:i]):
            if num2 < num1 and sums[j] + num1 >= sums[i]:
                sums[i] = sums[j] + num1
                sequences[i] = j
            if sums[i] > sums[max_sum_idx]:
                max_sum_idx = i

    return (sums[max_sum_idx], build_sequence(nums, sequences, max_sum_idx))


def build_sequence(nums: List[int],
                   sequences: List[Optional[int]],
                   current_idx: Optional[int]) -> List[int]:
    sequence: List[int] = []
    while current_idx is not None:
        sequence.append(nums[current_idx])
        current_idx = sequences[current_idx]
    return list(reversed(sequence))


print(max_sum_increasing_subsequence([8, 12, 15,  7]))
