
def findCelebrity(n: int) -> int:
    candidate = 0

    for i in range(n):
        if knows(candidate, i):
            candidate = i

    for j in range(n):
        if candidate == j:
            continue

        if knows(candidate, j) or not knows(j, candidate):
            return -1

    return candidate

