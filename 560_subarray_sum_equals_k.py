from typing import List
from collections import defaultdict

def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    sm = 0
    sum_freqs = defaultdict(int)
    sum_freqs[0] = 1

    for i in range(len(nums)):
        sm += nums[i]
        count += sum_freqs[sm - k]
        sum_freqs[sm] += 1

    return count

