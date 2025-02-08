from collections import defaultdict
import heapq

class NumberContainer:
    def __init__(self):
        self.indexes = defaultdict(int)
        self.min_heaps = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.indexes[index] = number
        heapq.heappush(self.min_heaps[number], index)

    def find(self, number: int) -> int:
        min_heap = self.min_heaps[number]

        while min_heap:
            index = min_heap[0]
            if self.indexes[index] == number:
                return index
            heapq.heappop(min_heap)

        return -1

