from typing import List
from collections import defaultdict

def countGood(nums: List[int], k: int) -> int:
    n = len(nums)
    counts = defaultdict(int)
    l, res, pairs = 0, 0, 0

    for r in range(n):
        pairs += counts[nums[r]]
        counts[nums[r]] += 1

        while pairs >= k:
            res += n - r

            counts[nums[l]] -= 1
            pairs -= counts[nums[l]]
            l += 1

    return res

