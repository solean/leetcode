from typing import List

def unique_paths_without_obstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    if obstacleGrid[0][0] == 1:
        return 0

    for r in range(m):
        for c in range(n):
            if obstacleGrid[r][c] == 1:
                obstacleGrid[r][c] = 'X'

    for i in range(n - 1, -1, -1):
        if obstacleGrid[m - 1][i] == 'X':
            # Found right-most obstacle on bottom row
            break
        else:
            obstacleGrid[m - 1][i] = 1

    for i in range(m - 1, -1, -1):
        if obstacleGrid[i][n - 1] == 'X':
            # Found bottom-most obstacle on last column
            break
        else:
            obstacleGrid[i][n - 1] = 1


    for r in range(m - 2, -1, -1):
        for c in range(n - 2, -1, -1):
            if obstacleGrid[r][c] == 'X':
                continue

            right = obstacleGrid[r][c + 1]
            if right == 'X': right = 0

            bottom = obstacleGrid[r + 1][c]
            if bottom == 'X': bottom = 0

            obstacleGrid[r][c] = right + bottom

    return obstacleGrid[0][0]