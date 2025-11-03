from typing import List
import heapq

def minCost(colors: str, neededTime: List[int]) -> int:
    time = 0
    multiples = [neededTime[0]]
    curr_color = colors[i]

    for i in range(1, len(colors)):
        if colors[i] == curr_color:
            heapq.heappush(multiples, neededTime[i])
        else:
            while len(multiples) > 1:
                time += heapq.heappop(multiples)
            curr_color = colors[i]
            multiples = [neededTime[i]]

    while len(multiples) > 1:
        time += heapq.heappop(multiples)

    return time

