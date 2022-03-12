
def climbing_stairs(n):
    a = 1
    b = 1

    for i in range(n - 2, -1, -1):
        a, b = a + b, a

    return a
