from typing import List

PRICES = {
    1: 800,
    2: 1520,
    3: 2160,
    4: 2560,
    5: 3000,

}


def find_sets(basket: List[int]) -> List[int]:
    copy = basket.copy()
    sets = []
    uniq = set(copy)
    while copy:
        sets.append(len(uniq))
        for b in uniq:
            copy.remove(b)
        uniq = set(copy)
    return sets


def total(basket: List[int]) -> int:
    set_lengths = find_sets(basket)
    # Amazing optimizations!!!
    while 3 in set_lengths and 5 in set_lengths:
        set_lengths.remove(3)
        set_lengths.remove(5)
        set_lengths.extend([4, 4])

    return sum(PRICES[set] for set in set_lengths)
