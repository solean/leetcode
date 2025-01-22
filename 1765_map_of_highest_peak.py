from typing import List
from collections import deque

def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    rows, cols = len(isWater), len(isWater[0])
    heights = [[0 for _ in range(cols)] for _ in range(rows)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    water_cells = []

    for r in range(rows):
        for c in range(cols):
            if isWater[r][c]:
                water_cells.append((r, c, 0))

    q = deque(water_cells)
    visited = set()
    while q:
        for _ in range(len(q)):
            (r, c, distance) = q.popleft()

            if (r, c) in visited:
                continue
            visited.add((r, c))

            heights[r][c] = distance

            for dr, dc in dirs:
                if (
                    0 <= r + dr < rows and
                    0 <= c + dc < cols and
                    (r + dr, c + dc) not in visited and
                    not isWater[r + dr][c + dc]
                ):
                    q.append((r + dr, c + dc, distance + 1))

    return heights

