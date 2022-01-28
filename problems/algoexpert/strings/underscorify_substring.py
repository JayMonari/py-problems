from typing import List


def get_locations(string: str, substring: str) -> List[List[int]]:
    locations: List[List[int]] = []
    substr_len = len(substring)
    start_idx = 0
    while start_idx < len(string):
        next_idx: int = string.find(substring, start_idx)
        if next_idx == -1:
            break
        locations.append([next_idx, next_idx + substr_len])
        start_idx = next_idx + 1
    return locations


def collapse(locations: List[List[int]]) -> List[List[int]]:
    collapsed_locations: List[List[int]] = [locations[0]]
    previous: List[int] = collapsed_locations[0]
    for idx in range(1, len(locations)):
        current = locations[idx]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            collapsed_locations.append(current)
            previous = current
    return collapsed_locations


def underscorify(string: str, locations):
    locations_idx = 0
    string_idx = 0
    in_between_underscores = False
    switch_idx = 0
    final_chars: List[str] = []
    while string_idx < len(string) and locations_idx < len(locations):
        if string_idx == locations[locations_idx][switch_idx]:
            final_chars.append("_")
            in_between_underscores = not in_between_underscores
            if not in_between_underscores:
                locations_idx += 1
            switch_idx = 0 if switch_idx == 1 else 1
        final_chars.append(string[string_idx])
        string_idx += 1
    if locations_idx < len(locations):
        final_chars.append("_")
    elif string_idx < len(string):
        final_chars.append(string[string_idx:])
    return "".join(final_chars)


def underscorify_substring(string: str, substring: str) -> str:
    locations: List[List[int]] = collapse(get_locations(string, substring))
    return underscorify(string, locations)


test, subtest = "testthis is a testtest to see if testestest it works", "test"
# _test_this is a _testtest_ to see if _testestest_ it works
print(underscorify_substring(test, subtest))
