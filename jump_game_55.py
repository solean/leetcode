from typing import List 
    
def can_jump(nums: List[int]) -> bool:
    dp = [None] * len(nums)
    dp[0] = nums[0]

    if len(nums) < 2 or nums[0] >= len(nums) - 1:
        return True
    if nums[0] == 0:
        return False

    for i in range(1, len(nums)):
        if nums[i] == 0 and dp[i - 1] <= i:
            return False

        dp[i] = max(dp[i - 1], i + nums[i])

        if dp[i] >= len(nums) - 1:
            return True