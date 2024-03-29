from typing import List

def three_sum_closest(nums: List[int], target: int) -> int:
    l = len(nums)
    nums = sorted(nums)
    closest = None
    
    for i in range(l):
        j = i + 1
        k = l - 1

        while j < k:
            sum_three = nums[i] + nums[j] + nums[k]
            if closest is None or (abs(sum_three - target) < abs(closest - target)):
                closest = sum_three

            if sum_three < target:
                j += 1
            elif sum_three > target:
                k -= 1
            else:
                closest = target
                break


    return closest

