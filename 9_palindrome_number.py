
def isPalindrome(x: int) -> bool:
    s = str(x)
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
        elif l % 2 == 0 and j == int(len(s)/2):
            break
        else:
            i += 1
            j -= 1

    return True


# TODO:
def isPalindromeWithoutString(x: int) -> bool:
    return False

