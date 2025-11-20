from typing import List

def findFinalValue(nums: List[int], original: int) -> int:
    nums.sort()
    res = original

    for n in nums:
        if n == res:
            res *= 2

    return res

