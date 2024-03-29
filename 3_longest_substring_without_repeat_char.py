
def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    res = 0
    h = {}

    for r in range(len(s)):
        ch = s[r]
        while ch in h:
            h.pop(s[l])
            l += 1

        h[ch] = True
        res = max(res, r - l + 1)

    return res