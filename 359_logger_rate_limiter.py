
class Logger:

    def __init__(self):
        self.timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timestamps:
            self.timestamps[message] = timestamp + 10
            return True
        elif timestamp >= self.timestamps[message]:
            self.timestamps[message] = timestamp + 10
            return True
        else:
            return False

