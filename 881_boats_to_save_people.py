from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort(reverse = True)
    num_boats = 0

    l = 0
    r = len(people) - 1

    while l <= r:
        if people[l] == limit:
            l += 1
        elif people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            l += 1

        num_boats += 1

    return num_boats

