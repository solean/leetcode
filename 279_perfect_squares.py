
def num_squares(n: int) -> int:
    dp = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i] = i

        j = 1
        while j**2 <= i:
            dp[i] = min(dp[i], 1 + dp[i - j**2])
            j += 1

    return dp[n]