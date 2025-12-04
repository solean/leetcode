from typing import List
from collections import defaultdict
import heapq

def highFive(items: List[List[int]]) -> List[List[int]]:
    scores = defaultdict(list)
    for i, score in items:
        heapq.heappush(scores[i], score)

    averages = []
    for i in scores:
        while len(scores[i]) > 5:
            heapq.heappop(scores[i])
        averages.append([i, sum(scores[i]) // 5])

    averages.sort()
    return averages

