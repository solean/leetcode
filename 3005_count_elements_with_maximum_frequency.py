from typing import List
from collections import Counter

def maxFrequencyElements(nums: List[int]) -> int:
    max_freq = 0

    counter = Counter(nums)

    for n in counter:
        max_freq = max(max_freq, counter[n])
    
    num_with_max = 0

    for n in counter:
        if counter[n] == max_freq:
            num_with_max += max_freq
    
    return num_with_max
