from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.wsum = sum(w)
        self.prefixsum = [0] * len(w)
        self.prefixsum[0] = w[0]
        for i in range(1, len(w)):
            self.prefixsum[i] = self.prefixsum[i - 1] + w[i]

    def pickIndex(self) -> int:
        target = self.wsum * random.random()
        l = 0
        r = len(self.prefixsum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefixsum[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l

