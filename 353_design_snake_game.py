from typing import List

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food

        self.pos = (0, 0)
        self.tail = []
        self.score = 0

        self.dirs = {
            "U": (-1, 0),
            "D": (1, 0),
            "R": (0, 1),
            "L": (0, -1)
        }

    def move(self, direction: str) -> int:
        x, y = self.pos
        dx, dy = self.dirs[direction]
        nx, ny = x + dx, y + dy

        if nx >= self.height or nx < 0 or ny >= self.width or ny < 0:
            return -1

        if self.food and [nx, ny] == self.food[0]:
            self.score += 1
            self.food.pop(0)
            self.tail.insert(0, (x, y))
        else:
            if self.tail:
                self.tail.pop()
                self.tail.insert(0, (x, y))

        if (nx, ny) in self.tail:
            return -1

        self.pos = (nx, ny)

        return self.score

