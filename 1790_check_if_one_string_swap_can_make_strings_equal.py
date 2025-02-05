
def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    diffs = []
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            diffs.append([s1[i], s2[i]])

    if len(diffs) == 2 and diffs[0] == list(reversed(diffs[1])):
        return True

    return False

