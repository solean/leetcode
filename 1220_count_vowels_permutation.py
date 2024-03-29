
def count_vowel_permutations(n: int) -> int:
    mod = 10**9 + 7
    dp = [[1, 1, 1, 1, 1]]

    for i in range(1, n):
        #      a  e  i  o  u
        row = [0, 0, 0, 0, 0]
        last = dp[i - 1]

        # a
        row[0] = (last[1] + last[2] + last[4]) % mod
        # e
        row[1] = (last[0] + last[2]) % mod
        # i
        row[2] = (last[1] + last[3]) % mod
        # o
        row[3] = last[2]
        # u
        row[4] = last[2] + last[3]

        dp.append(row)

    return sum(dp[-1]) % mod