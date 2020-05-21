
def can_construct(ransom_note: str, magazine: str) -> bool:
    mag_char_counts = dict()
    for ch in magazine:
        if ch in mag_char_counts:
            mag_char_counts[ch] += 1
        else:
            mag_char_counts[ch] = 1

    ransom_char_counts = dict()
    for ch in ransom_note:
        if ch not in mag_char_counts:
            return False

        if ch in ransom_char_counts:
            ransom_char_counts[ch] += 1
            if ransom_char_counts[ch] > mag_char_counts[ch]:
                return False
        else:
            ransom_char_counts[ch] = 1

    return True

