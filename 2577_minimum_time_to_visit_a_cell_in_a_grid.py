from typing import List
import heapq

def minimumTime(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1

    pq = [(grid[0][0], 0, 0)]
    grid[0][0] = -1

    while pq:
        time, r, c = heapq.heappop(pq)

        if r == rows - 1 and c == cols - 1:
            return time

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                wait_time = 1 if (grid[nr][nc] - time) % 2 == 0 else 0
                next_time = max(grid[nr][nc] + wait_time, time + 1)
                heapq.heappush(pq, (next_time, nr, nc))
                grid[nr][nc] = -1

    return -1

