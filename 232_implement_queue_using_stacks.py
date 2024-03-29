class MyQueue:

    def __init__(self):
        self.stack = []
        self.depot = []
        self.peek_item = None
    
    def push(self, x: int) -> None:
        if not self.stack:
            self.peek_item = x
        
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.depot.append(self.stack.pop())
        
        to_pop = self.depot.pop()

        if self.depot:
            self.peek_item = self.depot[-1]
        else:
            self.peek_item = None
        
        while self.depot:
            self.stack.append(self.depot.pop())
        
        return to_pop

    def peek(self) -> int:
        return self.peek_item

    def empty(self) -> bool:
        if self.stack:
            return False
        return True