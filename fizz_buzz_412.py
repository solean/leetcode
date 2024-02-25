from typing import List

def fizzBuzz(n: int) -> List[str]:
    ans = []

    for i in range(1, n + 1):
        a = ""

        if i % 3 == 0:
            a += "Fizz"
        if i % 5 == 0:
            a += "Buzz"

        ans.append(a if a else str(i))

    return ans

