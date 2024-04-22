from typing import List
from collections import deque

def islandPerimeter(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    perimeter = 0
    q = deque()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # find island (problem states that there is exactly one island in the grid)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                q.append((r, c))
                visited.add((r, c))
                break

    while q:
        i, j = q.popleft()

        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols:
                if (x, y) not in visited:
                    if grid[x][y] == 1:
                        q.append((x, y))
                        visited.add((x, y))
                    else:
                        perimeter += 1
            else:
                perimeter += 1

    return perimeter
