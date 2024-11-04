
def compressedString(word: str) -> str:
    comp = ""

    while word:
        prefix = word[0]

        if len(word) == 1:
            word = ""
            comp += "1" + prefix
            break

        i = 1
        while i < len(word) and word[i] == prefix and i < 9:
            i += 1
        comp += str(i) + prefix
        word = word[i:]

    return comp

