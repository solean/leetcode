from typing import List

def canSortArrayON2(nums: List[int]) -> bool:
    n = len(nums)
    values = nums.copy()

    for i in range(n):
        for j in range(n - i - 1):
            if values[j] <= values[j + 1]:
                continue

            if bin(values[j]).count("1") == bin(values[j + 1]).count("1"):
                values[j], values[j + 1] = values[j + 1], values[j]
            else:
                return False

    return True

def canSortArrayOptimal(nums: List[int]) -> bool:

    def count_bits(n):
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res

    curr_min = nums[0]
    curr_max = nums[0]
    prev_max = float("-inf")

    for n in nums:
        if bin(n).count("1") == bin(curr_min).count("1"):
            curr_min = min(curr_min, n))
            curr_max = min(curr_max, n))
        else:
            if curr_min < prev_max:
                # can't swap
                return False
            else:
                prev_max = curr_max
                curr_min = n
                curr_max = n

    if curr_min < prev_max:
        return False

    return True

