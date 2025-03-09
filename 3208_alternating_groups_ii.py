from typing import List

def numberOfAlternatingGroups(colors: List[int], k: int) -> int:
    # create "circle"
    for i in range(k - 1):
        colors.append(colors[i])

    res = 0
    l, r = 0, 1

    while r < len(colors):
        if colors[r] == colors[r - 1]:
            l = r
            r += 1
            continue

        r += 1
        if r - l < k:
            continue

        res += 1
        l += 1

    return res

