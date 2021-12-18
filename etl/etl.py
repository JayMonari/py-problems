from typing import Dict, List


def transform(data: Dict[int, List[str]]) -> Dict[str, int]:
    return {v.lower(): k for k, sub_list in data.items() for v in sub_list}
