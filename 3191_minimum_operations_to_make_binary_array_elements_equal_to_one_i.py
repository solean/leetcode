from typing import List

def minOperations(nums: List[int]) -> int:
    res = 0

    for i in range(len(nums) - 2):
        if nums[i] == 0:
            nums[i] = 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            res += 1

    return res if all(nums) else -1

