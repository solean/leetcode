from typing import List

def stringMatching(words: List[str]) -> List[str]:

    def is_substr(a, b):
        if len(a) > len(b):
            return False

        for i in range(len(b) - len(a) + 1):
            if a == b[i:i+len(a)]:
                return True

        return False

    res = set()
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] != words[j]:
                if is_substr(words[i], words[j]):
                    res.add(words[i])

    return list(res)

