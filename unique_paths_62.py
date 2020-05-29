
# Naive recursive solution -> too slow
def unique_paths_recursive(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    right = unique_paths(m - 1, n)
    down = unique_paths(m, n - 1)
    return right + down


# Faster math solution
def unique_paths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    counts = [[0 for x in range(m)] for y in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == n-1 and j == m-1:
                counts[i][j] = 0
            elif i == n-1 or j == m-1:
                counts[i][j] = 1
            else:
                counts[i][j] = counts[i+1][j] + counts[i][j+1]

    return counts[0][0]

