from typing import List

def largestAltitude(gain: List[int]) -> int:
    n = len(gain)
    pfs = [0] * (n + 1)
    mx = 0

    for i in range(1, n + 1):
        pfs[i] = pfs[i - 1] + gain[i - 1]
        mx = max(mx, pfs[i])

    return mx

