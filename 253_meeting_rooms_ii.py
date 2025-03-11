from typing import List
import heapq

def minMeetingRooms(intervals: List[List[int]]) -> int:
    intervals.sort()
    min_heap = []
    max_used = 0

    for start, end in intervals:
        if min_heap and start >= min_heap[0]:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, end)

        max_used = max(max_used, len(min_heap))

    return max_used

