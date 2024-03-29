
def detect_capital_use(word: str) -> bool:
    if len(word) < 2:
        return True

    if word[0].isupper():
        upper = word[1].isupper()
        for ch in word[2:]:
            if ch.isupper() != upper:
                return False

        return True
    else:
        upper = word[1].isupper()
        if upper == True:
            return False

        for ch in word[2:]:
            if ch.isupper() != upper:
                return False

        return True