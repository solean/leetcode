
def longest_palindrome(s: str) -> int:
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    max_length = 0
    counts = sorted(list(d.values()), reverse=True)
    odd = False
    for count in counts:
        if count % 2 == 0:
            max_length += count
        else:
            odd = True
            max_length += count - 1

    if odd:
        max_length += 1

    return max_length
