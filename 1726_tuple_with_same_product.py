from typing import List
from collections import defaultdict

def tupleSameProduct(nums: List[int]) -> int:
    n = len(nums)
    prod_freqs = defaultdict(int)

    for i in range(n):
        for j in range(i + 1, n):
            prod_freqs[nums[i] * nums[j]] += 1


    res = 0
    for freq in prod_freqs.values()
        pairs = count * (count - 1) // 2
        res += 8 * pairs
    return res

