
def longest_palindromic_substring(s: str) -> str:
    le = len(s)
    longest = ''

    for i in range(le):
        # check for odd length palindromes
        l, r = i, i
        while l >= 0 and r < le and s[l] == s[r]:
            pal = s[l:r + 1]
            if len(pal) > len(longest):
                longest = pal
            l -= 1
            r += 1

        # also check for evens
        l, r = i, i + 1
        while l >= 0 and r < le and s[l] == s[r]:
            pal = s[l:r + 1]
            if len(pal) > len(longest):
                longest = pal
            l -= 1
            r += 1

    longest = longest or s[0]
    return longest



# Expect: 'bab'
# longest_palindromic_substring('babad')
# Expect: 'bb'
# longest_palindromic_substring('cbbd')
# longest_palindromic_substring('abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa')
# longest_palindromic_substring('ac')
# longest_palindromic_substring('bb')
# longest_palindromic_substring('abb')