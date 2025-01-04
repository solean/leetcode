
def countPalindromicSubsequences(s: str) -> int:
    count = 0

    letters = set(s)
    for letter in letters:
        i = s.index(letter)
        j = s.rindex(letter)
        between = set()

        for k in range(i + 1, j):
            between.add(s[k])

        count += len(between)

    return count

