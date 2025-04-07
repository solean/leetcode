from typing import List

def shortestDistance(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def bfs(distances, r, c):
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque([(r, c)])
        visited = set()
        visited.add((r, c))

        steps = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 0:
                    distances[r][c][0] += steps
                    distances[r][c][1] += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 0
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            steps += 1


    total_houses = 0
    distances = [[[0, 0] for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                total_houses += 1
                bfs(distances, r, c)

    min_distance = float("inf")

    for r in range(rows):
        for c in range(cols):
            if distances[r][c][1] == total_houses:
                min_distance = min(min_distance, distances[r][c][0])

    return min_distance if min_distance < float("inf") else -1

