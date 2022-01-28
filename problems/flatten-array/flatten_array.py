from typing import Iterable, List


def flatten(nested: Iterable) -> List[int]:
    flat: List[int] = []
    for val in nested:
        if isinstance(val, (list, tuple, set)):
            flat.extend(flatten(val))
        elif isinstance(val, int):
            flat.append(val)
    return flat
