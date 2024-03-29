from collections import defaultdict

def can_construct(ransom_note: str, magazine: str) -> bool:
    chars = defaultdict(int)

    for mch in magazine:
        chars[ch] += 1

    for rch in ransom_note:
        if chars[rch] == 0:
            return False
        chars[rch] -= 1

    return True

