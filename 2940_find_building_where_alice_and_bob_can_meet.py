from typing import List
import heapq

def leftmostBuildingQueries(heights: List[int], queries: List[List[int]]) -> List[int]:
    ans = [-1] * len(queries)
    min_heap = []
    store_queries = [[] for _ in range(len(heights))]

    for i, (a, b) in enumerate(queries):
        if a == b:
            ans[i] = a
        elif a < b and heights[a] < heights[b]:
            ans[i] = b
        elif a > b and heights[a] > heights[b]:
            ans[i] = a
        else:
            store_queries[max(a, b)].append((max(heights[a], heights[b]), i))

    for i, height in enumerate(heights):
        while min_heap and min_heap[0][0] < height:
            _, qi = heapq.heappop(min_heap)
            ans[qi] = i

        for item in store_queries[i]:
            heapq.heappush(min_heap, item)

    return ans

