from collections import Counter
from typing import List

def countStudents(students: List[int], sandwiches: List[int]) -> int:
    n = len(students)
    fed = 0

    for i in range(n):
        swich = sandwiches[i]
        if counts[swich]:
            fed += 1
            counts[swich] -= 1
        else:
            break

    return n - fed

