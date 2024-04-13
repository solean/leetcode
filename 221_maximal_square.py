from typing import List

def maximalSquare(matrix: List[List[str]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    max_side = 0

    dp = [[0 for j in range(cols + 1)] for i in range(rows + 1)]
    for i in range(rows - 1,-1,-1):
        for j in range(cols - 1,-1,-1):
            if matrix[i][j] == "1":
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
                max_side = max(max_side, dp[i][j])
    
    return max_side ** 2
    