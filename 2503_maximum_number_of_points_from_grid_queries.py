from typing import List
import heapq

def maxPoints(grid: List[List[int]], queries: List[int]) -> List[int]:
    rows, cols = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = [0] * len(queries)

    queries_sorted = [(val, i) for i, val in enumerate(queries)]
    queries_sorted.sort()

    min_heap = []
    min_heap.append((grid[0][0], 0, 0))
    visited = set()
    visited.add((0, 0))
    points = 0

    for query_val, query_i in queries_sorted:
        while min_heap and min_heap[0][0] < query_val:
            cell_val, row, col = heapq.heappop(min_heap)
            points += 1

            for dr, dc in dirs:
                if (
                    0 <= row + dr < rows
                    and 0 <= col + dc < cols
                    and (row + dr, col + dc) not in visited
                ):
                    heapq.heappush(min_heap, (grid[row + dr][col + dc], row + dr, col + dc))
                    visited.add((row + dr, col + dc))

        res[query_i] = points

    return res

