
def find_least_num_of_unique_ints(arr: List[int], k: int) -> int:
    counts = Counter(arr)
    least_common = list(reversed(counts.most_common()))
    i = 0

    while k > 0:
        n, count = least_common[i]

        if count > k:
            counts[n] -= count - k
            k = 0
        else:
            k -= count
            del counts[n]
            i += 1

    return len(counts)

