
def minTimeToVisitAllPoints(points) -> int:
    res = 0

    for i in range(len(points) - 1):
        x, y = points[i]
        nx, ny = points[i + 1]
        res += max(abs(nx - x), abs(ny - y))

    return res

