from typing import List
from collections import defaultdict

def findChampion(n: int, edges: List[List[int]]) -> int:
    rev = defaultdict(list)
    for a, b in edges:
        rev[b].append(a)

    champs = []
    for i in range(n):
        if not rev[i]:
            if champs:
                return -1
            else:
                champs.append(i)

    return champs[0] if len(champs) == 1 else -1

