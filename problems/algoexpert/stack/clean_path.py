from typing import Iterator, List


def is_important_token(t: str): return len(t) != 0 and t != '.'


def shorten_path(path: str) -> str:
    ROOT_MARKER = ""
    PARENT_DIR = ".."
    is_absolute_path = path[0] == '/'
    stack: List[str] = []
    if is_absolute_path:
        stack.append(ROOT_MARKER)

    tokens: Iterator[str] = filter(is_important_token, path.split('/'))
    for token in tokens:
        if token == PARENT_DIR:
            if len(stack) == 0 or stack[-1] == PARENT_DIR:
                stack.append(token)
            elif stack[-1] != ROOT_MARKER:
                stack.pop()
        else:
            stack.append(token)
    if len(stack) == 1 and stack[0] == ROOT_MARKER:
        return "/"
    return "/".join(stack)


test1 = "/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../.."
test2 = "../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../.."
test3 = "/foo/./././bar/./baz///////////test/../../../ppa"
print(shorten_path(test1), shorten_path(test2), shorten_path(test3))
