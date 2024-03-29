from collections import Counter

def customSortString(order: str, s: str) -> str:
    freq = Counter(s)
    new_str = ""
    seen = set()

    for ch in order:
        if ch in freq:
            new_str += ch * freq[ch]
            seen.add(ch)
    
    for ch in s:
        if ch not in seen:
            new_str += ch
    
    return new_str
