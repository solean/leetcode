from collections import defaultdict

def numberOfStrings(s: str) -> int:
    l, r = 0, 0
    res = 0
    counts = defaultdict(int)

    def is_valid():
        return (
            counts["a"] > 0 and
            counts["b"] > 0 and
            counts["c"] > 0
        )

    while r < len(s):
        counts[s[r]] += 1

        while is_valid():
            res += len(s) - r
            counts[s[l]] -= 1
            l += 1

        r += 1

    return res

