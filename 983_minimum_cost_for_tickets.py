from typing import List

def mincostTickets(days: List[int], costs: List[int]) -> int:
    dp = {}

    def dfs(day):
        if day >= len(days):
            return 0
        if day in dp:
            return dp[day]

        dp[day] = float("inf")
        for d, cost in zip([1, 7, 30], costs):
            i = day
            while i < len(days) and days[i] < days[day] + d:
                i += 1
            dp[day] = min(dp[day], cost + dfs(i))

        return dp[day]

    return dfs(0)

