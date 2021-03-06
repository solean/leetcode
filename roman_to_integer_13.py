
def romanToInt(s: str) -> int:
    num = 0
    i = 0

    while i < len(s):
        ch = s[i]
        next_ch = s[i + 1] if i < len(s) - 1 else None

        if ch == 'I':
            if next_ch == 'V':
                num += 4
                i += 1
            elif next_ch == 'X':
                num += 9
                i += 1
            else:
                num += 1
        elif ch == 'V':
            num += 5
        elif ch == 'X':
            if next_ch == 'L':
                num += 40
                i += 1
            elif next_ch == 'C':
                num += 90
                i += 1
            else:
                num += 10
        elif ch == 'L':
            num += 50
        elif ch == 'C':
            if next_ch == 'D':
                num += 400
                i += 1
            elif next_ch == 'M':
                num += 900
                i += 1
            else:
                num += 100
        elif ch == 'D':
            num += 500
        elif ch == 'M':
            num += 1000
    
        i += 1

    return num

