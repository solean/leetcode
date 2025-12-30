from typing import List

def countNegatives(grid: List[List[int]]) -> int:
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    i = 0

    for r in range(rows - 1, -1, -1):
        for c in range(i, cols):
            if grid[r][c] < 0:
                count += 1
            else:
                i = c + 1

    return count

