
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.deque:
            self.deque.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.deque:
            self.deque.pop(-1)
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) >= self.k

