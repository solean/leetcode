
def longestIdealString(s: str, k: int) -> int:
    dp = [0] * 26
    res = 0

    for i in range(len(s)):
        ch_val = ord(s[i]) - ord("a")
        best = 0

        # check prev dp for chs +/- k away from current ch
        for prev in range(max(0, ch_val - k), min(26, ch_val + k + 1)):
            best = max(best, dp[prev])

        dp[ch_val] = best + 1
        res = max(res, dp[ch_val])

    return res

