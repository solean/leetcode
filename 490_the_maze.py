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


def dfs_solution(maze, start, dest) -> bool:
    rows, cols = len(maze), len(maze[0])
    visited = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def roll(x, y, dx, dy):
        nx, ny = x, y
        while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
            nx += dx
            ny += dy
        return nx, ny

    def dfs(x, y):
        if [x, y] == destination:
            return True
        if (x, y) in visited:
            return False
        visited.add((x, y))

        for dx, dy in dirs:
            nx, ny = roll(x, y, dx, dy)
            if dfs(nx, ny):
                return True

        return False

    return dfs(start[0], start[1])

