from typing import List

def is_palindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def first_palindrome(words: List[int]) -> str:
    for word in words:
        if is_palindrome(word):
            return word

    return ""

