from typing import List


def merge_sort_helper(main_array: List[int],
                      start_idx: int,
                      end_idx: int,
                      auxiliary_array: List[int],
                      iteration: int) -> None:
    if start_idx == end_idx:
        return

    mid_idx = start_idx + (end_idx - start_idx) // 2
    merge_sort_helper(
        auxiliary_array, start_idx, mid_idx, main_array, iteration + 1)
    merge_sort_helper(
        auxiliary_array, mid_idx + 1, end_idx, main_array, iteration + 1)
    merge(main_array, start_idx, mid_idx, end_idx, auxiliary_array)


def merge(main_array: List[int],
          start_idx: int,
          mid_idx: int,
          end_idx: int,
          auxiliary_array: List[int]) -> None:
    main_idx = start_idx
    left_idx = start_idx
    right_idx = mid_idx + 1
    while left_idx <= mid_idx and right_idx <= end_idx:
        if auxiliary_array[left_idx] <= auxiliary_array[right_idx]:
            main_array[main_idx] = auxiliary_array[left_idx]
            left_idx += 1
        else:
            main_array[main_idx] = auxiliary_array[right_idx]
            right_idx += 1
        main_idx += 1
    while left_idx <= mid_idx:
        main_array[main_idx] = auxiliary_array[left_idx]
        left_idx += 1
        main_idx += 1
    while right_idx <= end_idx:
        main_array[main_idx] = auxiliary_array[right_idx]
        right_idx += 1
        main_idx += 1


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    auxiliary_array = nums[:]
    iteration = 0
    merge_sort_helper(nums, 0, len(nums) - 1, auxiliary_array, iteration)
    return nums


test: List[int] = [
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
print(merge_sort(test))
