from typing import List

def minOperations(boxes: str) -> List[int]:
    ans = [0] * len(boxes)

    for i in range(len(boxes)):
        count = 0
        for j in range(len(boxes)):
            if boxes[j] == "1" and i != j:
                count += abs(i - j)
        ans[i] = count

    return ans

