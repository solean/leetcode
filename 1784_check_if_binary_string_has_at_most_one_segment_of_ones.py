
def checkOnesSegment(s: str) -> bool:
    num_ones = s.count("1")

    n = 0
    for i in range(len(s)):
        if s[i] == "0":
            break
        else:
            n += 1

    if num_ones > n:
        return False

    return True

