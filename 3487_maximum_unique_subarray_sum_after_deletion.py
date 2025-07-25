from typing import List
from collections import Counter

def maxSum(nums: List[int]) -> int:
    if max(nums) < 0:
        return max(nums)

    max_sum = 0
    counts = Counter(nums)

    for n in counts:
        if n > 0:
            max_sum += n

    return max_sum

