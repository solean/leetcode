from typing import List

def max_profit(prices: List[int]) -> int:
    profit = 0
    n = len(prices)

    for i in range(0, n - 1):
        diff = prices[i + 1] - prices[i]
        profit = max(profit, profit + diff)

    return profit

