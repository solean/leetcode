
# Naive recursive solution -> too slow
def unique_paths_recursive(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    right = unique_paths(m - 1, n)
    down = unique_paths(m, n - 1)
    return right + down


# Faster dp solution
def unique_paths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    dp = [[1 for _ in range(m)] for _ in range(n)]

    for r in range(m - 2, -1, -1):
        for c in range(n - 2, -1, -1):
            dp[r][c] = dp[r][c + 1] + dp[r + 1][c]

    return dp[0][0]
