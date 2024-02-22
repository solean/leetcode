
def mergeAlternately(word1: str, word2: str) -> str:
    smaller_len = len(word1) if len(word1) < len(word2) else len(word2)
    new_str = ""

    for i in range(smaller_len):
        new_str += word1[i]
        new_str += word2[i]

    if i < len(word1) - 1:
        new_str += word1[i+1:]
    elif i < len(word2) - 1:
        new_str += word2[i+1:]

    return new_str

