

def lengthOfLongestSubstring(s: str) -> int:
    longest = 1
    l = len(s)
    if l == 0:
        return 0
    elif l == 1:
        return 1

    i = 0
    while i < l:
        seen = {}
        for j in range(i, l):
            ch = s[j]
            if ch in seen:
                if j - i > longest:
                    longest = j - i
                break
            elif j == l - 1:
                if j - i + 1 > longest:
                    longest = j - i + 1
            else:
                seen[ch] = True
        i += 1

    print(longest)
    return longest


# Expect: 3
lengthOfLongestSubstring('abcabcbb')
# Expect: 1
lengthOfLongestSubstring('bbbbb')
# Expect: 3
lengthOfLongestSubstring('pwwkew')
# Expect: 2
lengthOfLongestSubstring('au')
