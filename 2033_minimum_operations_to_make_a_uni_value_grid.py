from typing import List

def minOperations(self, grid: List[List[int]], x: int) -> int:
    flattened = [item for row in grid for item in row]
    flattened.sort()

    n = len(flattened)
    med = flattened[n // 2]
    res = 0

    for num in flattened:
        if num % x != med % x:
            return -1
        else:
            res += (abs(num - med) // x)

    return res

