
def addBinary(a: str, b: str) -> str:
    res = ""
    # reverse a and b
    a, b = a[::-1], b[::-1]

    carry = 0
    maxlen = max(len(a), len(b))
    for i in range(maxlen):
        # ord(a[i]) - ord("0") computes to 0 or 1
        digitA = ord(a[i]) - ord("0") if i < len(a) else 0
        digitB = ord(b[i]) - ord("0") if i < len(b) else 0

        total = digitA + digitB + carry
        ch = str(total % 2)
        res = ch + res
        carry = total // 2

    if carry == 1:
        res = "1" + res

    return res

