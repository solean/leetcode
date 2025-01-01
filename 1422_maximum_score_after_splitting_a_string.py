from collections import Counter

def maxScore(s: str) -> int:
    counts = Counter(s)
    num_ones = counts["1"]

    curr_score = 1 + num_ones if s[0] == "0" else num_ones - 1
    max_score = curr_score

    for i in range(1, len(s) - 1):
        if s[i] == "0":
            curr_score += 1
            max_score = max(max_score, curr_score)
        else:
            curr_score -= 1

    return max_score

