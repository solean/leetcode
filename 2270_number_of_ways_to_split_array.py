from typing import List

def waysToSplitArray(nums: List[int]) -> int:
    forward = [0] * len(nums)
    forward[0] = nums[0]
    for i in range(1, len(nums)):
        forward[i] = forward[i - 1] + nums[i]

    backward = [0] * len(nums)
    backward[-1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        backward[i] = backward[i + 1] + nums[i]

    count = 0
    for i in range(len(nums) - 1):
        if forward[i] >= backward[i + 1]:
            count += 1

    return count

