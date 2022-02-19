from typing import List


def get_permutations(nums: List[int]) -> List[List[int]]:
    permutations: List[List[int]] = []
    permutations_helper(0, nums, permutations)
    return permutations


def permutations_helper(i: int, nums: List[int],
                        permutations: List[List[int]]) -> None:
    if i == len(nums) - 1:
        permutations.append(nums[:])
        return

    for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        permutations_helper(i + 1, nums, permutations)
        nums[i], nums[j] = nums[j], nums[i]


print(get_permutations([1, 2, 3, 4]))
