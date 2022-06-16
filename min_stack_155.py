
class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []


    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min, val)

        self.stack.append(val)


    def pop(self) -> None:
        popped = self.stack.pop()

        if popped == self.min:
            if not self.stack:
                self.min = None
            else:
                new_min = self.stack[0]
                for n in self.stack[1:]:
                    new_min = min(new_min, n)
                self.min = new_min


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min
