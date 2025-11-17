from typing import List

def kLengthApart(nums: List[int], k: int) -> bool:
    if 1 not in nums:
        return True

    last_one = nums.index(1)

    for i in range(last_one + 1, len(nums)):
        if nums[i] == 1:
            if i - last_one > k:
                last_one = i
            else:
                return False

    return True

