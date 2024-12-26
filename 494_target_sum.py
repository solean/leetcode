from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
    dp = {}

    def dfs(i, curr_sum):
        if (i, curr_sum) in dp:
            return dp[(i, curr_sum)]

        if i == len(nums):
            return 1 if curr_sum == target else 0

        minus = dfs(i + 1, curr_sum - nums[i])
        plus = dfs(i + 1, curr_sum + nums[i])
        dp[(i, curr_sum)] = minus + plus
        return minus + plus

    return dfs(0, 0)

