from typing import List

def findMin(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    mn = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            return min(mn, nums[l])

        mid = (l + r) // 2
        mn = min(mn, nums[mid])

        if nums[l] <= nums[mid]: # left side
            l = mid + 1
        else: # right side
            r = mid - 1

    return mn