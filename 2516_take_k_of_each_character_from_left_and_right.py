from collections import Counter, defaultdict

def takeCharacters(s: str, k: int) -> int:
    counts = Counter(s)
    if counts["a"] < k or counts["b"] < k or counts["c"] < k:
        return -1

    window = defaultdict(int)
    max_window = 0
    l = 0
    for r in range(len(s)):
        window[s[r]] += 1

        while l <= r and (
            counts["a"] - window["a"] < k
            or counts["b"] - window["b"] < k
            or counts["c"] - window["c"] < k
        ):
            window[s[l]] -= 1
            l += 1

        max_window = max(max_window, r - l + 1)

    return len(s) - max_window

