from typing import List

def minimumMountainRemovals(nums: List[int]) -> int:
    n = len(nums)
    lis_dp = [1] * n
    lds_dp = [1] * n

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                lis_dp[i] = max(lis_dp[i], 1 + lis_dp[j])

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                lds_dp[i] = max(lds_dp[i], 1 + lds_dp[j])

    min_removals = n
    for i in range(n):
        if min(lis_dp[i], lds_dp[i]) > 1:
            min_removals = min(min_removals, n - lis_dp[i] - lds_dp[i] + 1)
    return min_removals

