from typing import List, Union


def product_sum(nums: List[Union[int, List[int]]], multiplier: int = 1) -> int:
    recursive_sum = 0
    for element in nums:
        if type(element) is list:
            recursive_sum += product_sum(element, multiplier + 1)
        else:
            recursive_sum += element
    return recursive_sum * multiplier


test = [
    9,
    [2, -3, 4],
    1,
    [1, 1, [1, 1, 1]],
    [[[[3, 4, 1]]], 8],
    [1, 2, 3, 4, 5, [6, 7], -7],
    [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
    [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]],
    -3
]
print(product_sum(test))
