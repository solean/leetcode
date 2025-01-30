from typing import List

def findMaxFish(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()

    def dfs(node):
        if (r, c) in visited:
            return 0
        visited.add((r, c))

        curr_fish = grid[r][c]

        for dr, dc in dirs:
            if (
                0 <= r + dr < rows and
                0 <= c + dc < cols and 
                (r + dr, c + dc) not in visited and 
                grid[r + dr][c + dc] > 0
            ):
                curr_fish += dfs(r + dr, c + dc)

        return curr_fish


    max_fish = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                max_fish = max(max_fish, dfs(r, c))

    return max_fish

