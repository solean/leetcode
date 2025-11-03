from typing import List
import heapq

def minCostOptimal(colors: str, neededTime: List[int]) -> int:
    time = 0
    curr_max = neededTime[0]
    curr_time = neededTime[0]

    for i in range(1, len(colors) + 1):
        if i < len(colors) and colors[i] == colors[i - 1]:
            curr_max = max(curr_max, neededTime[i])
            curr_time += neededTime[i]
        else:
            time += (curr_time - curr_max)
            if i < len(colors):
                curr_max = neededTime[i]
                curr_time = neededTime[i]

    return time


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

