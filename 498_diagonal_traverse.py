from typing import List
from collections import defaultdict

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    rows = len(mat)
    cols = len(mat[0])
    diags = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            diags[r + c].append(mat[r][c])

    ans = []
    for r in diags.keys():
        diag = diags[r]
        if r % 2 == 0:
            diag.reverse()
        ans.extend(diag)

    return ans

