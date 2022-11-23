from typing import List
from collections import deque

def solve_maze(maze: List[List[int]], start: List[int], dest: List[int]) -> bool:
    m = len(maze)
    n = len(maze[0])

    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque()

    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        square = q.pop()
        if square == dest:
            print(dest)
            return True

        for direction in directions:
            i = square[0] + direction[0]
            j = square[1] + direction[1]
            while 0 <= i <= n and 0 <= j <= n and maze[i][j] == 0:
                i += direction[0]
                j += direction[1]

            # track back since last increment broke the while rule
            i -= direction[0]
            j -= direction[1]

            if not visited[i][j]:
                q.append([i, j])
                visited[i][j] = True

    return False
