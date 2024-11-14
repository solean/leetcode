from typing import List
import math

def minimizedMaximum(n: int, quantities: List[int]) -> int:

    def can_distribute(k):
        if k == 0:
            return False

        num_stores = 0
        for q in quantities:
            num_stores += math.ceil(q / k)

        return num_stores <= n


    max_quant = max(quantities)
    l = 0
    r = max_quant
    min_max = max_quant

    while l <= r:
        mid = (l + r) // 2
        if can_distribute(mid):
            min_max = mid
            r = mid - 1
        else:
            l = mid + 1

    return min_max

