from typing import List
from collections import defaultdict

def maximumUniqueSubarray(nums: List[int]) -> int:
    counts = defaultdict(int)

    max_sum = 0
    curr_sum = 0
    l, r = 0, 0

    while r < len(nums):
        while counts[nums[r]] > 0:
            counts[nums[l]] -= 1
            curr_sum -= nums[l]
            l += 1

        counts[nums[r]] += 1
        curr_sum += nums[r]
        max_sum = max(max_sum, curr_sum)
        r += 1

    return max_sum

