from collections import Counter


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    intersection: list[int] = []
    counter1 = Counter(nums1)
    for num2 in nums2:
        counter1[num2] -= 1
        if counter1[num2] >= 0:
            intersection.append(num2)
    return intersection


def intersect2(nums1: list[int], nums2: list[int]) -> list[int]:
    intersection: list[int] = []
    nums1.sort()
    nums2.sort()
    len1, len2 = len(nums1), len(nums2)
    idx1, idx2 = 0, 0
    while idx1 < len1 and idx2 < len2:
        if nums1[idx1] < nums2[idx2]:
            idx1 += 1
        elif nums1[idx1] > nums2[idx2]:
            idx2 += 1
        else:
            intersection.append(nums1[idx1])
            idx1 += 1
            idx2 += 1
    return intersection
