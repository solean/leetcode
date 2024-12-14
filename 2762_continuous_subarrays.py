from typing import List
import heapq

def continuousSubarrays(nums: List[int]) -> int:
    count = 0

    min_heap = []
    max_heap = []
    i, j = 0, 0

    while j < len(nums):
        heapq.heappush(min_heap, (nums[j], j))
        heapq.heappush(max_heap, (-nums[j], j))

        while i < j and -max_heap[0][0] - min_heap[0][0] > 2:
            i += 1

            while min_heap and min_heap[0][1] < i:
                heapq.heappop(min_heap)
            while max_heap and max_heap[0][1] < i:
                heapq.heappop(max_heap)

        count += j - i + 1
        j += 1

    return count


ans = continuousSubarrays([5, 4, 2, 4])
print(ans)
