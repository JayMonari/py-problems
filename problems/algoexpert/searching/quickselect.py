from typing import List


def quickselect(nums: List[int], k: int) -> int:
    position = k - 1
    start_idx = 0
    end_idx = len(nums) - 1
    while True:
        if start_idx > end_idx:
            raise Exception("This isn't recursive Quick Sort!")
        pivot_value = nums[start_idx]
        left_idx = start_idx + 1
        right_idx = end_idx
        while left_idx <= right_idx:
            if nums[left_idx] > pivot_value and nums[right_idx] < pivot_value:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
            if nums[left_idx] <= pivot_value:
                left_idx += 1
            if nums[right_idx] >= pivot_value:
                right_idx -= 1

        nums[start_idx], nums[right_idx] = nums[right_idx], nums[start_idx]
        if right_idx < position:
            start_idx = right_idx + 1
        elif right_idx > position:
            end_idx = right_idx - 1
        else:
            return nums[right_idx]


test, k = [102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5
print(quickselect(test, k))
