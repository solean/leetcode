from typing import List

def divideString(s: str, k: int, fill: str) -> List[str]:
    n = len(s)
    res = []
    i = 0

    while i < n:
        if i + k < n:
            res.append(s[i:i+k])
        else:
            temp = s[i:]
            temp += fill * (k - len(temp))
            res.append(temp)

        i += k

    return res

