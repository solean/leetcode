
def max_profit(prices) -> int:
    cur, max_so_far = 0, 0

    for i in range(1, len(prices)):
        cur = max(0, cur + prices[i] - prices[i - 1])
        max_so_far = max(max_so_far, cur)

    return max_so_far

