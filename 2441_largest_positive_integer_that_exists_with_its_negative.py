from typing import List
from collections import defaultdict

def findMaxK(nums: List[int]) -> int:
    maxint = -1
    d = defaultdict(int)

    for n in nums:
        if -n in d:
            maxint = max(maxint, abs(n))
        d[n] = True
    
    return maxint
