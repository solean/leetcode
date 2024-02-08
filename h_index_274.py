from typing import List

def hIndex(citations: List[int]) -> int:
    n = len(citations)
    citations.sort(reverse=True)

    for i in range(n, 0, -1):
        for j in range(n):
            if citations[j] >= i:
                if j + 1 == i:
                    return i
                continue
            else:
                break
    
    return 0
