from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    used = [False] * len(nums)

    def getperms(curr):
        if len(curr) == len(nums):
            # copy of curr
            res.append(curr[:])

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            curr.append(nums[i])
            getperms(curr)
            curr.pop()
            used[i] = False

    getperms([])
    return res

