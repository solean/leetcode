
def maxVowels(s: str, k: int) -> int:
    vowels = set(["a", "e", "i", "o", "u"])

    curr_vowels = sum([ch in vowels for ch in s[:k]])
    max_vowels = curr_vowels

    for i in range(k, len(s)):
        if s[i] in vowels:
            curr_vowels += 1
        if s[i - k] in vowels:
            curr_vowels -= 1
        max_vowels = max(max_vowels, curr_vowels)

    return max_vowels

