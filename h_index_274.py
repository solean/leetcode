from typing import List

def hIndex(citations: List[int]) -> int:
    n = len(citations)
    citations.sort()

    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    
    return 0
