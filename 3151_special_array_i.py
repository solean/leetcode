from typing import List

def isArraySpecial(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] % 2 == nums[i + 1] % 2:
            return False

    return True

