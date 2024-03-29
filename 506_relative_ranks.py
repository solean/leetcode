from typing import List
import heapq

def findRelativeRanks(score: List[int]) -> List[int]:
    max_heap = []
    n = len(score)
    output = [0] * n

    for i in range(n):
        heapq.heappush(max_heap, (-score[i], i))

    for i in range(n):
        _, indx = heapq.heappop(max_heap)

        if i == 0:
            output[indx] = "Gold Medal"
        elif i == 1:
            output[indx] = "Silver Medal"
        elif i == 2:
            output[indx] = "Bronze Medal"
        else:
            output[indx] = str(i + 1)

    return output

