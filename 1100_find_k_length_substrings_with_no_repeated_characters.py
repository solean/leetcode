from collections import Counter

def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    if k > len(s):
        return 0

    chars = Counter(s[:k])
    count = 0
    res = 0

    for i in range(len(s) - k + 1):
        if count == k:
            res += 1

        chars[s[i]] -= 1
        if chars[s[i]] == 0:
            del chars[s[i]]
            count -= 1

        if i + k < len(s):
            if not chars[s[i + k]]:
                count += 1
            chars[s[i + k]] += 1

    return res

