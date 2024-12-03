from typing import List

def addSpaces(s: str, spaces: List[int]) -> str:
    words = []
    start_index = 0

    for i in range(spaces):
        space_index = spaces[i]
        word = s[start_index:space_index]
        words.append(word)
        start_index = space_index

    last_word = s[start_index:]
    words.append(last_word)

    return " ".join(words)

