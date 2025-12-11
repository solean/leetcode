from typing import List

def countCoveredBuildings(n: int, buildings: List[List[int]]) -> int:
    res = 0
    xmm = {}
    ymm = {}

    for x, y in buildings:
        if x not in xmm:
            xmm[x] = [y, y]
        else:
            xmm[x] = [min(xmm[x][0], y), max(xmm[x][1], y)]

        if y not in ymm:
            ymm[y] = [x, x]
        else:
            ymm[y] = [min(ymm[y][0], x), max(ymm[y][1], x)]

    for x, y in buildings:
        if xmm[x][0] < y < xmm[x][1] and ymm[y][0] < x < ymm[y][1]:
            res += 1

    return res

