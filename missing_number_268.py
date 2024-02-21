from typing import List

def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    total_sum = (n * (n + 1)) // 2
    nums_sum = sum(nums)
    return total_sum - nums_sum

