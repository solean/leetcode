
def isValid(word: str) -> bool:
    vowels = set(['a', 'e', 'i', 'o', 'u'])

    if len(word) < 3:
        return False

    containsVowel = False
    containsConsonant = False

    for ch in word:
        if not ch.isdigit() and not ch.isalpha():
            return False

        if ch.lower() in vowels:
            containsVowel = True
        elif ch.isalpha():
            containsConsonant = True

    return containsVowel and containsConsonant

