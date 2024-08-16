from typing import List
from collections import defaultdict

def kthDistinct(arr: List[int], k: int) -> str:
    freq = defaultdict(int)
    for s in arr:
        freq[s] += 1

    for s in arr:
        if freq[s] == 1:
            if k == 1:
                return s
            k -= 1

    return ""

