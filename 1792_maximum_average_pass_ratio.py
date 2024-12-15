from typing import List
import heapq

def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:
    max_heap = []

    for pass_size, total in classes:
        delta = ((pass_size + 1) / (total + 1)) - (pass_size / total)
        heapq.heappush(max_heap, (-delta, total, pass_size))

    for i in range(extraStudents):
        delta, class_size, pass_size = heapq.heappop(max_heap)
        class_size += 1
        pass_size += 1
        new_delta = ((pass_size + 1) / (class_size + 1)) - (pass_size / class_size)
        heapq.heappush(max_heap, (-new_delta, class_size, pass_size))

    pass_ratios = 0
    for i in range(len(max_heap)):
        delta, class_size, pass_size = max_heap[i]
        pass_ratios += (pass_size / class_size)

    return pass_ratios / len(classes)

