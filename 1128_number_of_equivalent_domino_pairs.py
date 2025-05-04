from typing import List
from collections import defaultdict

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    seen = defaultdict(int)
    res = 0

    for i in range(len(dominoes)):
        x, y = dominoes[i]
        if y < x:
            x, y = y, x

        res += seen[(x, y)]
        seen[(x, y)] += 1

    return res

