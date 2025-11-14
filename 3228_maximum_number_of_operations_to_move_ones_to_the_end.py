
def maxOperations(s: str) -> int:
    res = 0
    count_ones = 0
    i = 0

    while i < len(s):
        if s[i] == '0':
            while i < len(s) - 1 and s[i + 1] == '0':
                i += 1
            res += count_ones
        else:
            count_ones += 1

        i += 1

    return res

