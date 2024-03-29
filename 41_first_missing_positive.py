from typing import List

def firstMissingPositiveOptimalSpace(nums: List[int]) -> int:
    n = len(nums)

    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1

    for i in range(n):
        idx = abs(nums[i]) - 1

        if 0 <= idx < n and nums[idx] > 0:
            nums[idx] = -1 * nums[idx]

    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1


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
