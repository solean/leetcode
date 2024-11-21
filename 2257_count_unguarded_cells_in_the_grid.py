from typing import List

def countUnguarded(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    grid = [[0 for _ in range(n)] for _ in range(m)]

    for wx, wy in walls:
        grid[wx][wy] = "W"

    for gx, gy in guards:
        grid[gx][gy] = "G"

    def dfs(x, y, d):
        if not (0 <= x < m and 0 <= y < n):
            return
        elif grid[x][y] in ("W", "G"):
            return

        if grid[x][y] == 0:
            grid[x][y] = "X"

        if d == "U":
            dfs(x - 1, y, d)
        elif d == "D":
            dfs(x + 1, y, d)
        elif d == "R":
            dfs(x, y + 1, d)
        elif d == "L":
            dfs(x, y - 1, d)

    for gx, gy in guards:
        dfs(gx - 1, gy, "U")
        dfs(gx + 1, gy, "D")
        dfs(gx, gy + 1, "R")
        dfs(gx, gy - 1, "L")

    num_unguarded = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                num_unguarded += 1

    return num_unguarded

