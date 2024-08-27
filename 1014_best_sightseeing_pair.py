from typing import List

def maxScoreSightseeingPair(values: List[int]) -> int:
    n = len(values)
    dp = [0] * n
    dp[0] = values[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1], values[i] + i)

    max_pair = 0
    for j in range(1, n):
        max_pair = max(max_pair, dp[j - 1] + values[j] - j)

    return max_pair

