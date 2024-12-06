from typing import List

def maxCount(banned: List[int], n: int, maxSum: int) -> int:
    banned_set = set(banned)
    num_ints = 0
    curr_sum = 0

    for i in range(1, n + 1):
        if i not in banned_set:
            if curr_sum + i > maxSum:
                break
            curr_sum += i
            num_ints += 1

    return num_ints

