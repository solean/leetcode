from typing import List

def jump(nums: List[int]) -> int:
    dp = [0] * len(nums)

    for i in range(len(nums)):
        max_jumps = nums[i]
        for j in range(1, max_jumps + 1):
            if i + j >= len(nums):
                break

            if not dp[i + j]:
                dp[i + j] = 1 + dp[i]
            else:
                dp[i + j] = min(dp[i + j], 1 + dp[i])

    return dp[-1]