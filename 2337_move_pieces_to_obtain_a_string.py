
def canChange(start: str, target: str) -> bool:
    if start.replace("_", "") != target.replace("_", ""):
        return False

    n = len(start)

    i, j = 0, 0

    while i < n and j < n:
        while i < n and start[i] == "_":
            i += 1
        while j < n and target[j] == "_":
            j += 1

        if i >= n and j >= n:
            return True
        elif i >= n or j >= n:
            return False

        if start[i] != target[j]:
            return False
        elif target[j] == "L" and i < j: # L can only move left
            return False
        elif target[j] == "R" and i > j: # R can only move right
            return False

        i += 1
        j += 1

    return True

