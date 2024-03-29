
def minimumLength(s: str) -> int:
    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        ch = s[i]

        while i <= j and s[i] == ch:
            i += 1
        while i <= j and s[j] == ch:
            j -= 1
    
    return max(0, j - i + 1)
