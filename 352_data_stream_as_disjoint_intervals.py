from typing import List

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.append([value, value])
        else:
            l = 0
            r = len(self.intervals)

            while l < r:
                mid = (l + r) // 2
                if self.intervals[mid][0] <= value:
                    l = mid + 1
                else:
                    r = mid

            pos = l

            if pos - 1 >= 0 and self.intervals[pos - 1][0] <= value <= self.intervals[pos - 1][1]:
                # value present in existing interval
                return
            elif 0 < pos < len(self.intervals) and value == self.intervals[pos - 1][1] + 1 and value == self.intervals[pos][0] - 1:
                # merge intervals
                self.intervals[pos - 1][1] = self.intervals[pos][1]
                self.intervals.pop(pos)
            elif pos - 1 >= 0 and value == self.intervals[pos - 1][1] + 1:
                self.intervals[pos - 1][1] = value
            elif pos < len(self.intervals) and value == self.intervals[pos][0] - 1:
                self.intervals[pos][0] = value
            else:
                self.intervals.append([value, value])

            self.intervals.sort()

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

