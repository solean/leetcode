from typing import List
import heapq

def minimumObstacles(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    min_obstacles = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    min_obstacles[0][0] = grid[0][0]
    priority_queue = [(min_obstacles[0][0], (0, 0))]

    while priority_queue:
        num_obstacles, cell = heapq.heappop(priority_queue)

        if cell == (rows - 1, cols - 1):
            return num_obstacles

        for dx, dy in dirs:
            nx, ny = cell[0] + dx, cell[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny):
                new_num = num_obstacles + grid[nx][ny]
                if new_num < min_obstacles[nx][ny]:
                    min_obstacles[nx][ny] = new_num
                    heapq.heappush(priority_queue, (new_num, (nx, ny)))

    return min_obstacles[-1][-1]

