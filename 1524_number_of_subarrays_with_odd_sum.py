from typing import List

def numOfSubarrays(arr: List[int]) -> int:
    n = len(arr)
    res = 0
    ps = 0
    odd, even = 0, 0
    MOD = 10**9 + 7

    for n in arr:
        ps += n
        if ps % 2 != 0:
            res = (res + 1 + even) % MOD
            odd += 1
        else:
            res = (res + odd) % MOD
            even += 1

    return res

