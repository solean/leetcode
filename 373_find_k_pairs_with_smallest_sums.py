import heapq
from typing import List

def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = []

    for i in range(len(nums1)):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    smallest = []

    while len(smallest) < k:
        sm, i, j = heapq.heappop(heap)
        smallest.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return smallest

