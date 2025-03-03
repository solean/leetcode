from typing import List

def minSwaps(data: List[int]) -> int:
    total_ones = data.count(1)
    l = 0
    curr_ones = 0
    max_ones = 0

    for r in range(len(data)):
        if data[r] == 1:
            curr_ones  += 1

        if r - l >= total_ones:
            if data[l] == 1:
                curr_ones -= 1
            l += 1

        max_ones = max(max_ones, curr_ones)

    return total_ones - max_ones

