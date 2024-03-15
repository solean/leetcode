from typing import List

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    ans = 0
    freq = [0] * (len(nums) + 1)
    freq[0] = 1
    total_sum = 0

    for n in nums:
        total_sum += n
        if total_sum >= goal:
            ans += freq[total_sum - goal]
        
        freq[total_sum] += 1

    return ans
