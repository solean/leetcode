from typing import List

def maximum_bags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    # Sort by remaining capacity (capacity[i] - rocks[i])
    remaining = [(i, capacity[i] - rocks[i]) for i in range(len(rocks))]
    remaining.sort(key=lambda x: x[1])

    num_full = 0
    for x in remaining:
        if x[1] == 0:
            num_full += 1
            continue
        else:
            if x[1] > additionalRocks:
                break

            additionalRocks -= x[1]
            num_full += 1

        if not additionalRocks:
            break

    return num_full