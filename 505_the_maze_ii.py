from typing import List
import heapq

def shortestDistance(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    m, n = len(maze), len(maze[0])
    distances = [[float('inf') for _ in range(n)] for _ in range(m)]
    distances[start[0]][start[1]] = 0
    minheap = [(0, start)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while minheap:
        dist, (x, y) = heapq.heappop(minheap)
        if [x, y] == destination:
            return dist

        for dx, dy in dirs:
            nx, ny = x, y
            traveled = 0
            while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
                traveled += 1

            if traveled and dist + traveled <= distances[nx][ny]:
                heapq.heappush(minheap, (dist + traveled, [nx, ny]))
                distances[nx][ny] = dist + traveled


    return -1

