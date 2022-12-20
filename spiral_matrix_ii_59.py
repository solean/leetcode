from typing import List

def generate_matrix(n: int) -> List[List[int]]:
    l = 0
    r = n - 1
    t = 0
    b = n - 1
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    x = 1

    while l < r and t < b:

        for i in range(l, r + 1):
            matrix[t][i] = x
            x += 1
        t += 1

        for i in range(t, b + 1):
            matrix[i][r] = x
            x += 1
        r -= 1

        if l >= r or t >= b:
            break

        for i in range(r, l - 1, -1):
            matrix[b][i] = x
            x += 1
        b -= 1

        for i in range(b, t - 1, -1):
            matrix[i][l] = x
            x += 1
        l += 1

    mid = n // 2
    if n % 2 == 0:
        matrix[mid][mid - 1] = n*n
    else:
        matrix[mid][mid] = n*n

    return matrix