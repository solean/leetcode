from typing import List

def runningSum(self, nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums
    
    running_sum = [0 for i in range(len(nums))]
    running_sum[0] = nums[0]
    
    for i in range(1, len(nums)):
        running_sum[i] = running_sum[i - 1] + nums[i]
        
    return running_sum
