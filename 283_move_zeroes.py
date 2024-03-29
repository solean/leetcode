from typing import List


def moveZeroes(nums: List[int]) -> None:
    last = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[last] = nums[last], nums[i]
            last += 1


def moveZeroes2024Submission(nums: List[int]) -> None:
    i, j = 0, 0

    while j < len(nums):
        if nums[j]:
            nums[i] = nums[j]
            i += 1

        j += 1

    for k in range(i, len(nums)):
        nums[k] = 0

