from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    res = 0
    l, r = 0, len(nums) - 1

    while i < j:
        sm = nums[l] + nums[r]
        if sm == k:
            res += 1
            l += 1
            r -= 1
        elif sm > k:
            r -= 1
        else:
            l += 1

    return res

