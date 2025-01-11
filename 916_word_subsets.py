from typing import List
from collections import Counter, defaultdict

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    res = []

    sub_max = defaultdict(int)

    for word in words2:
        word_counts = Counter(word)
        for ch in word:
            sub_max[ch] = max(sub_max[ch], word_counts[ch])

    for word in words1:
        word_counts = Counter(word)
        word_valid = True
        for ch in word:
            if word_counts[ch] < sub_max[ch]:
                word_valid = False
                break

        if word_valid:
            res.append(word)

    return res

