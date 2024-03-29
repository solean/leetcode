from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # sort intervals by start value
    intervals = sorted(intervals)

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        last_end = merged[-1][1]

        if interval[0] <= last_end:
            merged[-1][1] = max(last_end, interval[1])
        else:
            merged.append(interval)

    return merged