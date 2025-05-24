from typing import List

def findWordsContaining(words: List[str], x: str) -> List[int]:
    res = []

    for i in range(len(words)):
        if x in words[i]:
            res.append(i)

    return res

