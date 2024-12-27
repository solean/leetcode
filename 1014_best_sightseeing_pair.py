from typing import List

def maxScoreSightseeingPairSpaceOptimal(values: Listp[int]) -> int:
    max_score = 0
    curr_max = values[0] - 1

    for i in range(1, len(values)):
        max_score = max(max_score, values[i] + curr_max)
        curr_max = max(curr_max - 1, values[i] - 1)

    return max_score


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

