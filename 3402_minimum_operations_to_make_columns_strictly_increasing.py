from typing import List

def minimumOperations(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    num_ops = 0

    if rows < 2:
        return 0

    for r in range(1, rows):
        for c in range(cols):
            if grid[r][c] <= grid[r - 1][c]:
                num_ops += (grid[r - 1][c] + 1) - grid[r][c]
                grid[r][c] = grid[r - 1][c] + 1

    return num_ops

