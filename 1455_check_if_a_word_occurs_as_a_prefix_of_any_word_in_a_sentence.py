
def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split(" ")
    n = len(searchWord)

    for i, word in enumerate(words):
        if word[:n] == searchWord:
            return i + 1

    return -1

