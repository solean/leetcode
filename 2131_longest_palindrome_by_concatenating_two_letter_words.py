from typing import List
from collections import Counter

def longestPalindrome(words: List[str]) -> int:
    counts = Counter(words)
    res = 0
    already_one_more = False

    for word in counts:
        if not counts[word]:
            continue

        ch1, ch2 = word
        rev = ch2 + ch1

        if word == rev:
            if counts[word] % 2 == 0:
                res += 2 * counts[word]
            else:
                res += 2 * (counts[word] - 1)
                if not already_one_more:
                    res += 2
                already_one_more = True
        elif rev in counts:
            n = min(counts[word], counts[rev])
            counts[word] -= n
            counts[rev] -= n
            res += 4 * n

    return res

