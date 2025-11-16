
def numSub(s: str) -> int:
    res = 0
    curr = 0
    MOD = 10**9 + 7

    for i in range(len(s)):
        if s[i] == '1':
            curr += 1
        else:
            if curr:
                res += (curr + 1) * curr // 2
            curr = 0

    if curr:
        res += (curr + 1) * curr // 2

    return res

