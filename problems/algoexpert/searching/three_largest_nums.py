from typing import List


def get_three_largest(nums: List[int]) -> List[int]:
    if len(nums) < 4:
        return nums

    three_largest: List[int] = nums[:3]
    three_largest.sort()
    for num in nums[3:]:
        if num > three_largest[2]:
            update(three_largest, num, 2)
        elif num > three_largest[1]:
            update(three_largest, num, 1)
        elif num > three_largest[0]:
            update(three_largest, num, 0)
    return three_largest


def update(three_largest: List[int], num: int, end_idx: int) -> None:
    for idx in range(end_idx + 1):
        if idx == end_idx:
            three_largest[idx] = num
        else:
            three_largest[idx] = three_largest[idx + 1]


print(get_three_largest([-3, -7, -17, -27, -18, -1, - 541, -8, -7, -2, 7]))
print(get_three_largest([1, 3, 8, 99]))
