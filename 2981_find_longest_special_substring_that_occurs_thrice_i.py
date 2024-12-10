import heapq
from collections import defaultdict

def maximumLength(s: str) -> int:
    n = len(s)
    dp = [1] * n
    for i in range(1, n):
        if s[i] == s[i - 1]:
            dp[i] = dp[i - 1] + 1

    alpha_groups = defaultdict(list)
    for i in range(n):
        ch = s[i]
        if len(alpha_groups[ch]) < 3:
            heapq.heappush(alpha_groups[ch], dp[i])
        else:
            if dp[i] > alpha_groups[ch][0]:
                heapq.heappop(alpha_groups[ch])
                heapq.heappush(alpha_groups[ch], dp[i])

    max_val = -1

    for ch in alpha_groups.keys():
        if len(alpha_groups[ch]) == 3:
            max_val = max(max_val, min(alpha_groups[ch]))

    return max_val

