from typing import List
from collections import defaultdict

def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    res = [0] * len(A)

    freqs = defaultdict(int)
    count = 0

    for i in range(0, len(A)):
        freqs[A[i]] += 1
        freqs[B[i]] += 1

        if freqs[A[i]] % 2 == 0:
            count += 1
        if A[i] != B[i] and freqs[B[i]] % 2 == 0:
            count += 1

        res[i] = count

    return res

