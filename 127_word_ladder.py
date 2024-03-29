from typing import List
from collections import deque


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    q = deque([(beginWord, 1)])
    visited = set([beginWord])

    while q:
        word, seq = q.popleft()
        if word == endWord:
            return seq

        for i in range(len(word)):
            for uni in range(ord('a'), ord('z') + 1):
                ch_arr = list(word)
                ch_arr[i] = chr(uni)
                neighbor_word = "".join(ch_arr)

                if neighbor_word in word_set and neighbor_word not in visited:
                    q.append((neighbor_word, seq + 1))
                    visited.add(neighbor_word)

    return 0
