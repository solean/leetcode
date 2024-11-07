from typing import List

def numEnclaves(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    num_ones = 0
    num_edge_ones = 0

    def dfs(x, y):
        nonlocal num_edge_ones
        num_edge_ones += 1
        visited.add((x, y))

        for dx, dy in dirs:
            if (0 <= x + dx < rows and
                0 <= y + dy < cols and
                grid[x + dx][y + dy] == 1 and
                (x + dx, y + dy) not in visited):

                dfs(x + dx, y + dy)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                num_ones += 1

            if (r in [0, rows - 1] or c in [0, cols - 1]) and
                grid[r][c] == 1 and
                (r, c) not in visited:

                dfs(r, c)

    return num_ones - num_edge_ones

