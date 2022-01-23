from typing import List


def build_max_heap(nums: List[int]) -> None:
    first_parent_idx = (len(nums) - 2) // 2
    for curr_idx in reversed(range(first_parent_idx + 1)):
        sift_down(curr_idx, len(nums) - 1, nums)


def sift_down(curr_idx: int, end_idx: int, heap: List[int]) -> None:
    child_idx1 = (curr_idx * 2) + 1
    swap_idx = -1
    while child_idx1 <= end_idx:
        child_idx2 = (curr_idx * 2) + 2
        if child_idx2 <= end_idx and heap[child_idx2] > heap[child_idx1]:
            swap_idx = child_idx2
        else:
            swap_idx = child_idx1
        if heap[swap_idx] < heap[curr_idx]:
            return

        heap[curr_idx], heap[swap_idx] = heap[swap_idx], heap[curr_idx]
        curr_idx = swap_idx
        child_idx1 = (curr_idx * 2) + 1


def heap_sort(nums: List[int]) -> List[int]:
    build_max_heap(nums)
    for end_idx in reversed(range(1, len(nums))):
        nums[0], nums[end_idx] = nums[end_idx], nums[0]
        sift_down(0, end_idx - 1, nums)
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
print(heap_sort(test))
