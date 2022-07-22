from typing import List
import collections

def max_area_of_island(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    max_area = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def bfs(r, c):
        print(r, c)
        island_area = 1
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q.append((r, c))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc

                if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):

                    q.append((r, c))
                    visited.add((r, c))
                    island_area += 1
                    max_area = max(max_area, island_area)

    for r in rows:
        for c in cols:
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)

    return max_area
