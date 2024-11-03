
def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    doubled = s + s
    i = 0
    j = len(s)

    while j < len(doubled):
        if doubled[i:j] == goal:
            return True
        i += 1
        j += 1

    return False

