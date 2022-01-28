from typing import List


def slices(series: str, length: int) -> List[str]:
    if len(series) < length:
        raise ValueError("Length must be smaller then string size.")
    elif length < 1:
        raise ValueError("Length must be a non-zero positive integer.")

    return [series[i:i+length] for i in range(0, len(series) - length + 1)]
