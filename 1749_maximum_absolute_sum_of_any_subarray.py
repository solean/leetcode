from typing import List

def maxAbsoluteSum(nums: List[int]) -> int:
    n = len(nums)

    max_dp = [0] * n
    max_dp[0] = nums[0]
    min_dp = [0] * n
    min_dp[0] = nums[0]

    for i in range(1, n):
        max_dp[i] = max(nums[i], max_dp[i - 1] + nums[i])
        min_dp[i] = min(nums[i], min_dp[i - 1] + nums[i])

    return max(max(max_dp), -min(min_dp))

