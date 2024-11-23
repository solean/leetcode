
def isOneEditDistance(s: str, t: str) -> bool:
    if s == t or abs(len(s) - len(t)) > 1:
        return False

    i = 0
    j = 0
    edited = False

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            if edited:
                return False

            if len(s) == len(t):
                # substitution
                i += 1
                j += 1
            elif len(s) < len(t):
                # insertion
                j += 1
            else:
                # deletion
                i += 1

            edited = True

    if i < len(s) or j < len(t):
        return not edited

    return True

