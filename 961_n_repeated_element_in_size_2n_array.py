from typing import List
from collections import Counter

def repeatedNTimes(nums: List[int]) -> int:
    counts = Counter(nums)
    n = len(counts) - 1

    for key in counts:
        if counts[key] == n:
            return key

    return -1

