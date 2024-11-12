
def validWordAbbreviation(word: str, abbr: str) -> bool:
    i, j = 0, 0

    def isdigit(ch):
        return 48 <= ord(ch) <= 57

    while j < len(abbr):
        if i < len(word) and word[i] == abbr[j]:
            i += 1
            j += 1
        elif isdigit(abbr[j]):
            num_str = ""
            while j < len(abbr) and isdigit(abbr[j]):
                num_str += abbr[j]
                j += 1
            if num_str[0] == "0":
                return False
            num = int(num_str)
            for _ in range(num):
                i += 1
                if i > len(word):
                    return False
        else:
            return False

    if i > len(word) or i < len(word):
        return False

    return True

