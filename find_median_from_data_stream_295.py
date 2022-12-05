import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.large and -self.small[0] > self.large[0]:
            small = -heapq.heappop(self.small)
            heapq.heappush(self.large, small)

        if len(self.small) - len(self.large) > 1:
            small = -heapq.heappop(self.small)
            heapq.heappush(self.large, small)

        if len(self.large) - len(self.small) > 1:
            large = heapq.heappop(self.large)
            heapq.heappush(self.small, -large)


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            if len(self.small) > len(self.large):
                return -self.small[0]
            else:
                return self.large[0]