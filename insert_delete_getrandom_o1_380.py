import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index = self.map[val]
        end_index = len(self.arr) - 1
        end_val = self.arr[end_index]

        self.arr[index], self.arr[end_index] = self.arr[end_index], self.arr[index]
        self.map[end_val] = index

        del self.map[val]
        self.arr.pop()

        return True

    def get_random(self) -> int:
        return random.choice(self.arr)
