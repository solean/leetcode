from typing import List
from collections import defaultdict

def equalPairs(grid: List[List[int]]) -> int:
    rows = defaultdict(list)
    cols = defaultdict(list)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            val = grid[r][c]
            rows[r].append(val)
            cols[c].append(val)

    count = 0
    for r in rows:
        for c in cols:
            if rows[r] == cols[c]:
                count += 1

    return count

