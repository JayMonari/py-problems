def move_zeroes(nums: list[int]) -> None:
    zero_idx = 0
    for idx in range(len(nums)):
        if nums[idx] == 0:
            continue
        nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
        zero_idx += 1
