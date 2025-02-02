from typing import List
from collections import Counter

def distinctNumbers(nums: List[int], k: int) -> List[int]:
    res = []
    counts = Counter(nums[:k])
    curr_distinct = len(counts)
    res.append(curr_distinct)

    for i in range(len(nums) - k):
        n = nums[i]
        counts[n] -= 1

        if counts[n] == 0:
            del counts[n]
            curr_distinct -= 1

        nxt = nums[i + k]
        if nxt not in counts:
            curr_distinct += 1
        counts[nxt] += 1

        res.append(curr_distinct)

    return res

