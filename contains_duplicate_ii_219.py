from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    curr = set()

    for i in range(k + 1):
        if i < len(nums):
            n = nums[i]
            if n in curr:
                return True
            curr.add(n)

    i = 0
    j = k
    while j < len(nums):
        curr.remove(nums[i])

        if j < len(nums) - 1:
            if nums[j + 1] in curr:
                return True
            curr.add(nums[j + 1])

        i += 1
        j += 1

    return Fals

