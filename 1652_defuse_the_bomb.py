from typing import List

def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    ans = [0] * n
    if k == 0:
        return ans

    start = 1
    end = k
    if k < 0:
        start = n - abs(k)
        end = k

    sm = sum(code[start:end + 1])
    for i in range(n):
        ans[i] = sm
        sm += code[(end + 1) % n]
        sm -= code[start % n]
        start += 1
        end += 1

    return ans

