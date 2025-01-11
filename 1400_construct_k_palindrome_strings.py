from collections import Counter

def canConstruct(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    counts = Counter(s)
    num_odd = 0
    for ch in counts:
        if counts[ch] % 2 != 0:
            num_odd += 1

    if num_odd > k:
        return False

    return True

