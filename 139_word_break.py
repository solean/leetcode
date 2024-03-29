from typing import List
from collections import deque

def word_break(s: str, word_dict: List[str]) -> bool:
    q = deque()
    q.append(0)
    visited = set()

    while q:
        i = q.popleft()
        if i not in visited:
            for word in word_dict:
                if s[i:i+len(word)] == word:
                    if i + len(word) == len(s):
                        # Reached end of string with a dictionary word
                        return True
                    else:
                        q.append(i + len(word))

            visited.add(i)

    return False