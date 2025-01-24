from typing import List
from collections import deque

def getFood(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    starting_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "*":
                starting_pos = (r, c)

    visited = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((starting_pos[0], starting_pos[1], 0))

    while q:
        for _ in range(len(q)):
            r, c, curr_path = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if grid[r][c] == "#":
                return curr_path

            for dr, dc in dirs:
                if (
                    0 <= r + dr < rows and
                    0 <= c + dc < cols and
                    (r + dr, c + dc) not in visited and
                    grid[r + dr][c + dc] != "X"
                ):
                    q.append((r + dr, c + dc, curr_path + 1))

    return -1

