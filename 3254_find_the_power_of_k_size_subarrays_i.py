from typing import List

def resultsArray(nums: List[int], k: int) -> List[int]:
    i = 0
    j = k - 1
    ans = []

    while j < len(nums):
        broke = False
        for k in range(i, j):
            if nums[k + 1] <= nums[k] or nums[k + 1] > nums[k] + 1:
                ans.append(-1)
                broke = True
                break
        if not broke:
            ans.append(nums[j])

        i += 1
        j += 1

    return ans

