from typing import List

def finalPrices(prices: List[int]) -> List[int]:
    n = len(prices)
    res = prices[:]

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] <= prices[i]:
                res[i] = prices[i] - prices[j]
                break

    return res

