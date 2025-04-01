from typing import List

def mostPoints(questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0] * n
    dp[-1] = questions[-1][0]

    for i in range(n - 2, -1, -1):
        curr = questions[i][0]
        if i + questions[i][1] + 1 < n:
            curr += dp[i + questions[i][1] + 1]
        dp[i] = max(curr, dp[i + 1])

    return max(dp)

