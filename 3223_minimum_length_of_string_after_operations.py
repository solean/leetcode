from collections import Counter

def minimumLength(self, s: str) -> int:
    l = len(s)
    freqs = Counter(s)

    for ch in freqs:
        if freqs[ch] >= 3:
            if freqs[ch] % 2 == 0:
                l -= (freqs[ch] - 2)
            else:
                l -= (freqs[ch] - 1)

    return l

