from typing import List

def min_path_sum(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if i == rows - 1 and j == cols - 1:
                dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]
                continue

            if i == rows - 1:
                dp[i][j] = grid[i][j] + dp[i][j + 1]
            elif j == cols - 1:
                dp[i][j] = grid[i][j] + dp[i + 1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]