from typing import List

def three_sum_closest(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    closest_diff = float('inf')
    closest_sum = None

    for n in nums:
        l = 0
        r = len(nums) - 1
        while l < r:
            three_sum = n + nums[l] + nums[r]
            diff = abs(three_sum - target)
            if diff < closest_diff:
                closest_diff = diff
                closest_sum = three_sum
            
            if three_sum < target:
                l += 1
            else:
                r -= 1

    return closest_sum