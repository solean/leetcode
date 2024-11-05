
def minChanges(s: str) -> int:
    changes = 0

    i = 0
    while i < len(s) - 1:
        if s[i] != s[i + 1]:
            changes += 1
        i += 2

    return changes

