from typing import List

def rob_partition(nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    return max(
        rob_partition(nums[:-1]),
        rob_partition(nums[1:])
    )