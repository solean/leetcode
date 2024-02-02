from typing import List
from collections import deque

def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    n = len(grid)
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, -1)]

    # x, y, path count
    q = deque([[0, 0, 0]])
    visited = set()
    visited.add((0, 0))

    while q:
        x, y, path = q.popleft()

        if x == n - 1 and y == n - 1:
            # we are at the bottom right of the grid (end of path)
            return path + 1
        else:
            for dx, dy in dirs:
                if ((x + dx, y + dy) not in visited and
                    0 <= x + dx <= n and
                    0 <= y + dy <= n and
                    grid[x + dx][y + dy] == 0):

                    visited.add((x + dx, y + dy))
                    q.append([x + dx, y + dy, path + 1])
    
    return -1
