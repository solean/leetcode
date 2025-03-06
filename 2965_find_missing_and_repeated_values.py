from typing import List

def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    res = [None, None]

    n = len(grid)
    seen = set()

    for r in range(n):
        for c in range(n):
            if grid[r][c] in seen:
                res[0] = grid[r][c]
            seen.add(grid[r][c])

    for i in range(1, n*n + 1):
        if i not in seen:
            res[1] = i
            break

    return res

