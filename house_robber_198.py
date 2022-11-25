from typing import List

def rob(nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]