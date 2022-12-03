from collections import Counter

def frequency_sort(s: str) -> str:
    counts = Counter(s)

    count_list = []
    for ch in counts:
        count_list.append([ch, counts[ch]])

    count_list.sort(key=lambda x: x[1], reverse=True)

    result = ""
    for c in count_list:
        result += c[0] * c[1]

    return result