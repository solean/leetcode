from typing import List
from collections import defaultdict

def findJudge(n: int, trust: List[List[int]]) -> int:
    trusts = defaultdict(int)
    for a, b in trust:
        trusts[a] += 1
    
    trusted = defaultdict(int)
    for a, b in trust:
        trusted[b] += 1
    
    for i in range(1, n + 1):
        if trusted[i] == n - 1 and not trusts[i]:
            return  i
    
    return -1
