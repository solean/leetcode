from collections import Counter

def canPermutePalindrome(s: str) -> bool:
    counts = Counter(s)
    num_odd = 0

    for count in counts.values():
        if count % 2 != 0:
            num_odd += 1

        if num_odd > 1:
            return False

    return True

