from typing import List

def divideArray(nums: List[int]) -> bool:
    nums.sort()

    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            i += 1
        else:
            return False

    return True


def divideArray2(nums):
    counts = Counter(nums)

    for count in counts.values():
        if count % 2 != 0:
            return False

    return True

