from typing import List

def min_falling_path_sum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    dp = [[None for _ in range(n)] for _ in range(n)]

    if n == 1:
        return matrix[0][0]

    def dfs(i, j):
        if i == n - 1:
            # last row
            return matrix[i][j]

        if dp[i][j] is not None:
            # already computed
            return dp[i][j]

        left = float('inf')
        right = float('inf')
        if j > 0:
            left = dfs(i + 1, j - 1)
        if j < n - 1:
            right = dfs(i + 1, j + 1)
        bottom = dfs(i + 1, j)

        min_path = matrix[i][j] + min(left, right, bottom)
        dp[i][j] = min_path
        return min_path

    for i in range(n):
        dfs(0, i)

    return min(dp[0])