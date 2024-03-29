
def num_decodings(s: str) -> int:
    dp = {}
    dp[len(s)] = 1

    for i in range(len(s) - 1, -1, -1):
        digit = s[i]

        if digit == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i < len(s) - 1 and (digit == '1' or (digit == '2' and int(s[i + 1]) <= 6)):
            dp[i] += dp[i + 2]

    return dp[0]