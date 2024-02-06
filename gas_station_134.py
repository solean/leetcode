from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    
    n = len(gas)
    total = 0
    start = 0

    for i in range(n):
        diff = gas[i] - cost[i]
        total += diff

        if total < 0:
            total = 0
            start = i + 1

    return start
