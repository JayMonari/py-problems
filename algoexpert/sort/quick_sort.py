from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    quick_sort_helper(nums, 0, len(nums) - 1)
    return nums


def quick_sort_helper(nums: List[int], start_idx: int, end_idx: int) -> None:
    if start_idx >= end_idx:
        return

    left_idx = start_idx + 1
    right_idx = end_idx
    pivot_value = nums[start_idx]
    while left_idx <= right_idx:
        if nums[left_idx] > pivot_value and nums[right_idx] < pivot_value:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
        if nums[left_idx] <= pivot_value:
            left_idx += 1
        if nums[right_idx] >= pivot_value:
            right_idx -= 1
    nums[start_idx], nums[right_idx] = nums[right_idx], nums[start_idx]
    leftside_len = right_idx - start_idx - 1
    rightside_len = end_idx - right_idx - 1
    if leftside_len < rightside_len:
        quick_sort_helper(nums, start_idx, right_idx - 1)
        quick_sort_helper(nums, right_idx + 1, end_idx)
    else:
        quick_sort_helper(nums, right_idx + 1, end_idx)
        quick_sort_helper(nums, start_idx, right_idx - 1)


test = [
    -19,
    759,
    168,
    306,
    270,
    -602,
    558,
    -821,
    -599,
    328,
    753,
    -50,
    -568,
    268,
    -92,
    381,
    -96,
    730,
    629,
    678,
    -837,
    351,
    896,
    63,
    -85,
    437,
    -453,
    -991,
    294,
    -384,
    -628,
    -529,
    518,
    613,
    -319,
    -519,
    -220,
    -67,
    834,
    619,
    802,
    207,
    946,
    -904,
    295,
    718,
    -740,
    -557,
    -560,
    80,
    296,
    -90,
    401,
    407,
    798,
    254,
    154,
    387,
    434,
    491,
    228,
    307,
    268,
    505,
    -415,
    -976,
    676,
    -917,
    937,
    -609,
    593,
    -36,
    881,
    607,
    121,
    -373,
    915,
    -885,
    879,
    391,
    -158,
    588,
    -641,
    -937,
    986,
    949,
    -321
]
print(quick_sort(test))
