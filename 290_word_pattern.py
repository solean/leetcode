
def wordPattern(pattern: str, s: str) -> bool:
    d = {}
    s_list = s.split(' ')
    seen = set()

    if len(pattern) != len(s_list):
        return False
    
    for i in range(len(pattern)):
        ch = pattern[i]
        word = s_list[i]

        if ch not in d:
            if word in seen:
                return False
            else:
                d[ch] = word
        elif d[ch] != word:
            return False

        seen.add(word)
    
    return True
