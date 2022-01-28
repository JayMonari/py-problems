from typing import Any, Callable, List


def append(list1: List[Any], list2: List[Any]) -> List[Any]:
    return [*list1, *list2]


def concat(lists: List[List[Any]]) -> List[Any]:
    return [v for sub_list in lists for v in sub_list]


def filter(fn: Callable[[Any], bool], _list: List[Any]) -> List[Any]:
    return [v for v in _list if fn(v)]


def length(list: List[Any]) -> int:
    return len(list)


def map(fn: Callable[[Any], Any], _list: List[Any]) -> List[Any]:
    return [fn(v) for v in _list]


def foldl(fn: Callable[[Any, Any], Any], _list: List[Any], initial: Any) -> Any:
    for v in _list:
        initial = fn(initial, v)
    return initial


def foldr(fn: Callable[[Any, Any], Any], _list: List[Any], initial: Any) -> List[Any]:
    for v in _list[::-1]:
        initial = fn(v, initial)
    return initial


def reverse(_list: List[Any]) -> List[Any]:
    return list(reversed(_list))
