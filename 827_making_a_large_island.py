from typing import List
from collections import defaultdict, deque

def largestIsland(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    island_size = defaultdict(int)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(start, island_num):
        r, c = start
        grid[r][c] = island_num
        island_size[island_num] += 1

        q = deque([start])

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 1:
                    grid[r + dr][c + dc] = island_num
                    island_size[island_num] += 1
                    q.append((r + dr, c + dc))


    curr_island_num = 2
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                bfs((r, c), curr_island_num)
                curr_island_num += 1

    all_ones = True
    largest = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                all_ones = False

                curr = 1
                seen = set()
                for dr, dc in dirs:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] > 0:
                        island_num = grid[r + dr][c + dc]
                        if island_num not in seen:
                            curr += island_size[island_num]
                        seen.add(island_num)
                largest = max(largest, curr)

    if all_ones:
        return rows * cols

    return largest

