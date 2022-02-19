from typing import List


def powerset(nums: List[int]) -> List[List[int]]:
    subsets: List[List[int]] = [[]]
    for element in nums:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [element])
    return subsets


print(powerset([1, 2, 3, 4, 5]))
