
def strStr(haystack: str, needle: str) -> int:
    if not str:
        return 0

    lh = len(haystack)
    ln = len(needle)

    if ln == lh:
        return 0 if needle == haystack else -1
    elif ln > lh:
        return -1

    for i in range(0, lh - ln + 1):
        sub = haystack[i:i+ln]
        if sub == needle:
            return i

    return -1

