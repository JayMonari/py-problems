def strStr(haystack: str, needle: str) -> int:
    if not haystack and not needle:
        return 0
    return haystack.find(needle)
