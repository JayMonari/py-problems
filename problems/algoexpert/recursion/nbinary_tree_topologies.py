from typing import Dict


def num_tree_topologies(n: int, cache: Dict[int, int] = {0: 1}) -> int:
    if n in cache:
        return cache[n]

    number_of_trees = 0
    for left_tree_size in range(n):
        right_tree_size = n - 1 - left_tree_size
        left_trees = num_tree_topologies(left_tree_size, cache)
        right_trees = num_tree_topologies(right_tree_size, cache)
        number_of_trees += left_trees * right_trees

    cache[n] = number_of_trees
    return cache[n]


print(num_tree_topologies(40))
