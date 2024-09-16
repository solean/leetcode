from typing import List

def findMinDifference(timePoints: List[str]) -> int:

    def convertToMinutes(time_str) -> int:
        hours = int(time_str[:2])
        minutes = int(time_str[3:])
        total_minutes = (hours * 60) + minutes
        return total_minutes

    timePoints = list(map(convert, timePoints))
    timePoints.sort()

    if timePoints[0] == 0:
        timePoints.append(1440)

    min_diff = float('inf')

    for i in range(len(timePoints) - 1):
        min_diff = min(min_diff, abs(timePoints[i] - timePoints[i + 1]))

    if timePoints[0] > 0:
        min_diff = min(min_diff, (1440 - timePoints[-1]) + timePoints[0])

    return min_diff

