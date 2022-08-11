def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    end_idx = m + n - 1
    idx1 = m - 1
    idx2 = n - 1
    while idx1 >= 0 and idx2 >= 0:
        if nums1[idx1] > nums2[idx2]:
            nums1[end_idx] = nums1[idx1]
            idx1 -= 1
        else:
            nums1[end_idx] = nums2[idx2]
            idx2 -= 1
        end_idx -= 1

    while idx2 >= 0:
        nums1[end_idx] = nums2[idx2]
        idx2 -= 1
        end_idx -= 1
    return nums1
