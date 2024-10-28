import math
from typing import List

def longestSquareStreak(nums: List[int]) -> int:
    num_set = set(nums)
    max_streak = -1

    for n in nums:
        if math.sqrt(n) not in num_set:
            streak = 1
            while n**2 in num_set:
                streak += 1
                n = n**2
            max_streak = max(max_streak, streak)

    return max_streak if max_streak >= 2 else -1

