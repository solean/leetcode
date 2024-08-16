from typing import List
from collections import defaultdict

def lemonadeChange(bills: List[int]) -> bool:
    onhand = defaultdict(int)

    while bills:
        bill = bills.pop(0)
        if bill == 5:
            onhand[5] += 1
        elif bill == 10:
            if onhand[5]:
                onhand[5] -= 1
                onhand[10] += 1
            else:
                return False
        elif bill == 20:
            if onhand[5] and onhand[10]:
                onhand[5] -= 1
                onhand[10] -= 1
                onhand[20] += 1
            elif onhand[5] > 2:
                onhand[5] -= 3
                onhand[20] += 1
            else:
                return False

    return True

