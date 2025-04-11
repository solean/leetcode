
def countSymmetricIntegers(low: int, high: int) -> int:
    res = 0

    i = low
    while i < high + 1:
        s = str(i)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            firsthalf = sum([int(ch) for ch in s[:mid]])
            secondhalf = sum([int(ch) for ch in s[mid:]])
            if firsthalf == secondhalf:
                res += 1
            i += 1
        else:
            s = "1" + ("0" * len(s))
            i = int(s)

    return res

