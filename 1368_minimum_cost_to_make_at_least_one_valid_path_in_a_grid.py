from typing import List
from collections import defaultdict, deque

def minCost(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    adj = defaultdict(list)
    dirs = [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]

    for r in range(rows):
        for c in range(cols):
            for dr, dc, arrow in dirs:
                if 0 <= r + dr < rows and 0 <= c + dc < cols:
                    weight = 0 if grid[r][c] == arrow else 1
                    adj[(r, c)].append((r + dr, c + dc, weight))

    q = deque([(0, 0, 0)])
    visited = set()

    while q:
        for _ in range(len(q)):
            r, c, curr_cost = q.popleft()

            if r == rows - 1 and c == cols - 1:
                return curr_cost

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nr, nc, cost in adj[(r, c)]:
                if cost == 0:
                    q.appendleft((nr, nc, curr_cost))
                else:
                    q.append((nr, nc, curr_cost + 1))

    return -1

