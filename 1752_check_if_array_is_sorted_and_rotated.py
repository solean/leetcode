from typing import List

def check(nums: List[int]) -> bool:
    nonsorted = []
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nonsorted.append(i + 1)


    if len(nonsorted) > 1:
        return False
    elif len(nonsorted) == 0:
        return True
    else:
        k = nonsorted[0]
        return nums[k:] + nums[:k] == sorted(nums)

