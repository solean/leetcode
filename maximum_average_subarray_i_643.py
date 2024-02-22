from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    i = 0
    j = k - 1

    curr_sum = sum(nums[i:j+1])
    max_avg = curr_sum / k

    i += 1
    j += 1
    while j < len(nums):
        curr_sum -= nums[i - 1]
        curr_sum += nums[j]
        avg = curr_sum / k
        max_avg = max(max_avg, avg)

        i += 1
        j += 1

    return max_avg

