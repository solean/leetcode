from typing import List
from collections import Counter
import math

def repairCars(ranks: List[int], cars: int) -> int:
    min_rank = min(ranks)
    max_rank = max(ranks)

    freqs = Counter(ranks)

    low = 1
    high = min_rank * cars * cars

    while low < high:
        mid = (low + high) // 2
        cars_repaired = 0

        for r in range(1, max_rank + 1):
            cars_repaired += freqs[r] * int(math.sqrt(mid // r))

        if cars_repaired >= cars:
            high = mid
        else:
            low = mid + 1

    return low

