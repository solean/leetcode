from typing import List

def maxAdjacentDistance(nums: List[int]) -> int:
    max_diff = 0

    for i in range(len(nums) - 1):
        max_diff = max(max_diff, abs(nums[i] - nums[i + 1]))

    max_diff = max(max_diff, abs(nums[0] - nums[-1]))

    return max_diff

