from typing import Callable, Counter, Iterator, List, Optional


def get_new_pattern(pattern: str) -> List[str]:
    pattern_letters = list(pattern)
    if pattern[0] == "x":
        return pattern_letters
    switch_x_and_y: Callable = lambda c: 'x' if c == 'y' else 'y'
    return list(map(switch_x_and_y, pattern_letters))


def find_first_y_position(pattern: str) -> Optional[int]:
    first_y_positon: Optional[int] = None
    for i, char in enumerate(pattern):
        if char == "y" and first_y_positon is None:
            first_y_positon = i
            break
    return first_y_positon


def pattern_matcher(pattern: str, string: str) -> List[str]:
    if len(string) < len(pattern):
        return []

    new_pattern: List[str] = get_new_pattern(pattern)
    did_switch: bool = new_pattern[0] != pattern[0]
    counter: Counter[str] = Counter(pattern)
    first_y_positon: Optional[int] = find_first_y_position(pattern)
    if first_y_positon == None:
        is_whole_num_x: bool = (len(string) / counter["x"]) % 1 == 0
        if not is_whole_num_x:
            return []

        len_of_x: int = int(len(string) / counter["x"])
        x: str = string[:len_of_x]
        potential_match: Iterator[str] = map(lambda _: x, new_pattern)
        if string == "".join(potential_match):
            return [x, ''] if not did_switch else ['', x]
    else:
        for len_of_x in range(1, len(string)):
            len_y: float = (len(string) - len_of_x *
                            counter["x"]) / counter["y"]
            if len_y <= 0 or len_y % 1 != 0:
                continue
            len_of_y: int = int(len_y)
            y_start_idx = first_y_positon * len_of_x
            y_end_idx = y_start_idx + len_of_y
            x: str = string[:len_of_x]
            y: str = string[y_start_idx:y_end_idx]
            potential_match: Iterator[str] = map(
                lambda char: x if char == "x" else y, new_pattern)
            if string == "".join(potential_match):
                return [x, y] if not did_switch else [y, x]
    return []


test, pat = "Fire! Fire! Dance with me!Fire! Fire! Dance with me!", "xxyxxy"
pat2, test2 = "xxxx", "GO!GO!GO!GO!"
print(pattern_matcher(pat, test))
print(pattern_matcher(pat2, test2))
