from typing import List
import math

def minimumSize(nums: List[int], maxOperations: int) -> int:

    def can_divide(max_balls):
        ops = 0
        for n in nums:
            ops += math.ceil(n / max_balls) - 1
            if ops > maxOperations:
                return False
        return True

    max_balls = max(nums)
    l = 1
    r = max_balls
    res = max_balls

    while l < r:
        mid = (l + r) // 2
        if can_divide(mid):
            r = mid
            res = mid
        else:
            l = mid + 1

    return res

