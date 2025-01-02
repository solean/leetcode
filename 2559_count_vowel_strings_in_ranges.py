from typing import List

def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    vowels = set(["a", "e", "i", "o", "u"])

    dp = [0] * len(words)
    dp[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0

    for i in rane(1, len(words)):
        dp[i] = dp[i - 1] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)

    ans = []
    for q0, q1 in queries:
        ans.append(dp[q1] - dp[q0 - 1] if q0 > 0 else dp[q1])

    return ans

