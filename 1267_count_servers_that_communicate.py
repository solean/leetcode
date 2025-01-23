from typing import List
from collections import defaultdict

def countServers(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    row_servers = defaultdict(set)
    col_servers = defaultdict(set)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                row_servers[r].add((r, c))
                col_servers[c].add((r, c))

    connected = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] and len(set(row_servers[r]).union(col_servers[c])) > 1:
                connected.update(row_servers[r], col_servers[c])

    return len(connected)

