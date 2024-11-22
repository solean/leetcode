from typing import List

def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[List[int]]:
    if not nums:
        return [[lower, upper]]

    missing = []

    if nums[0] > lower:
        missing.append([lower, nums[0] - 1])

    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            continue
        else:
            missing.append([nums[i] + 1, nums[i + 1] - 1])

    if nums[-1] < upper:
        missing.append([nums[-1] + 1, upper])

    return missing

