
def count_substrings(s: str) -> int:
    l = len(s)
    seen = dict()
    count = 0

    for i in range(l):
        for j in range(i + 1, l + 1):
            sub = s[i:j]
            if sub in seen:
                if seen[sub]:
                    count += 1
                else:
                    continue
            else:
                bool = is_palindrome(sub)
                seen[sub] = bool
                if bool:
                    count += 1

    return count

def is_palindrome(s: str) -> bool:
    l = len(s)
    if l == 0 or l == 1:
        return True
    elif l == 2:
        return s[0] == s[1]

    i = 0
    j = l - 1
    while i != j:
        if s[i] != s[j]:
            return False
        elif l % 2 == 0 and j == int(l / 2):
            break
        else:
            i += 1
            j -= 1
    return True

