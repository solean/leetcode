from typing import List

def maxMoves(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for j in range(cols - 2, -1, -1):
        for i in range(rows):
            val = grid[i][j]
            if j + 1 < cols and grid[i][j + 1] > val:
                dp[i][j] = max(dp[i][j], 1 + dp[i][j + 1])
            if i - 1 >= 0 and j + 1 < cols and grid[i - 1][j + 1] > val:
                dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j + 1])
            if i + 1 < rows and j + 1 < cols and grid[i + 1][j + 1] > val:
                dp[i][j] = max(dp[i][j], 1 + dp[i + 1][j + 1])

    return max(row[0] for row in dp)

