from typing import List
from collections import Counter

def findAnagrams(s: str, p: str) -> List[int]:
    res = []
    counts = Counter(p)
    window_counts = Counter(s[:len(p)])
    if counts == window_counts:
        res.append(0)

    i = 1
    j = len(p)
    while j < len(s):
        window_counts[s[i - 1]] -= 1
        window_counts[s[j]] += 1

        if window_counts == counts:
            res.append(i)

        i += 1
        j += 1

    return res

