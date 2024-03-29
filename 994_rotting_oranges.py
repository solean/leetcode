from typing import List
from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:
    minutes = 0
    q = deque()
    num_fresh = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                q.append([i, j])
            elif grid[i][j] == 1:
                num_fresh += 1

    if num_fresh == 0:
        return 0

    while q:
        minutes += 1

        for _ in range(len(q)):
            rotten = q.popleft()
            i = rotten[0]
            j = rotten[1]

            # check top, right, bottom, left
            if i > 0 and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                num_fresh -= 1
                q.append([i - 1, j])
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                num_fresh -= 1
                q.append([i, j + 1])
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                num_fresh -= 1
                q.append([i + 1, j])
            if j > 0 and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                num_fresh -= 1
                q.append([i, j - 1])

    if num_fresh:
        return -1

    return minutes - 1