from typing import List
from collections import deque

def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    m = len(maze)
    n = len(maze[0])

    visited = [[False for _ in range(n)] for _ in range(m)]
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    num_steps = 0

    if maze[entrance[0]][entrance[1]] == '+':
        return -1

    q = deque()
    q.append(entrance)
    visited[entrance[0]][entrance[1]] = True

    while q:
        for _ in range(len(q)):
            sq = q.popleft()
            val = maze[sq[0]][sq[1]]

            if sq != entrance and val == '.' and (sq[0] == 0 or sq[0] == m - 1 or sq[1] == 0 or sq[1] == n - 1):
                return num_steps

            for d in dirs:
                x = sq[0] + d[0]
                y = sq[1] + d[1]

                if 0 <= x < m and 0 <= y < n and maze[x][y] == '.' and not visited[x][y]:
                    visited[x][y] = True
                    q.append([x, y])

        num_steps += 1

    return -1