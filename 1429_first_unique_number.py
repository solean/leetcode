from typing import List
from collections import List

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.counts = Counter(nums)
        self.pointer = None

        for i in range(len(self.q)):
            if self.counts[self.q[i]] == 1:
                self.pointer = [i]
                break

    def showFirstUnique(self) -> int:
        return self.q[self.pointer] if self.pointer is not None else -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.counts[value] += 1

        if self.pointer is None and self.counts[value] == 1:
            self.pointer = len(self.q) - 1
        elif self.pointer is not None and self.q[self.pointer] == value:
            while self.pointer < len(self.q) and self.counts[self.q[self.pointer]] > 1:
                self.pointer += 1
            if self.pointer >= len(self.q):
                self.pointer = None

