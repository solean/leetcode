from typing import List

def applyOperations(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    zeros = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros.append(i)
        elif zeros:
            z = zeros.pop(0)
            nums[z] = nums[i]
            nums[i] = 0
            zeros.append(i)

    return nums

