from typing import List

def sort_colors(nums: List[int]):
    i = 0
    l = 0
    r = len(nums) - 1

    while i <= r:
        if nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        elif nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        else:
            i += 1
