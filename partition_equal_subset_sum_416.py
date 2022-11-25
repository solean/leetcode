from typing import List

def can_partition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    partition_total = int(total / 2)
    dp = [False] * (partition_total + 1)
    dp[0] = True

    for num in nums:
        for i in range(partition_total, -1, -1):
            if i >= num:
                dp[i] = dp[i] or dp[i - num]

    return dp[partition_total]