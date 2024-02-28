from typing import List
from collections import deque


def differ_by_one_letter(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    differences = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            differences += 1
            if differences > 1:
                return False
    
    return differences == 1


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    q = deque([(beginWord, 1)])

    while q:
        word, seq = q.popleft()
        if word == endWord:
            return seq
        
        for w in list(word_set):
            if differ_by_one_letter(word, w):
                q.append((w, seq + 1))
                word_set.remove(w)

    return 0
