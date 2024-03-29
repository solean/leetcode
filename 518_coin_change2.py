def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for i in range(len(coins) - 1, -1, -1):
        nextDP = [0] * (amount + 1)
        nextDP[0] = 1

        coin = coins[i]
        
        for a in range(1, amount + 1):
            nextDP[a] = dp[a]
            if a - coin >= 0:
                nextDP[a] += nextDP[a - coin]

        dp = nextDP

    return dp[amount]
    
