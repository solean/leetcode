
def first_unique_char(s: str) -> int:
    chars = dict()
    first_app = dict()

    for i in range(len(s)):
        ch = s[i]
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
            first_app[ch] = i
    

    for ch in chars:
        if chars[ch] == 1:
            return first_app[ch]
    
    return -1

