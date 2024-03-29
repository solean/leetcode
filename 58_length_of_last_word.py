
def easy_length_of_last_word(s: str) -> int:
    s = s.strip()
    return len(s.split(' ')[-1])

def length_of_last_word(s: str) -> int:
    words = []
    last_word = ''

    for ch in s:
        if ch == ' ':
            if last_word:
                words.append(last_word)
            last_word = ''
        else:
            last_word += ch

    if last_word:
        words.append(last_word)

    if len(words) == 0:
        return 0

    last_word = words[-1]
    return len(last_word)

