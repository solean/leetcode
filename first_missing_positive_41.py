from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    minint = float('inf')
    maxint = float('-inf')
    seen = set()

    for n in nums:
        if n > 0:
            minint = min(minint, n)
            maxint = max(maxint, n)
            seen.add(n)
        
    if minint > 1:
        return 1
    
    for i in range(minint + 1, maxint):
        if i not in seen:
            return i
    
    return maxint + 1
