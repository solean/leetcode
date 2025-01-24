from typing import List
from collections import defaultdict

def invalidTransactions(transactions: List[str]) -> List[str]:
    invalid = [False] * len(transactions)
    name_map = defaultdict(list)

    for i, tx in enumerate(transactions):
        name, time, amt, city = tx.split(",")
        name_map[name].append((i, name, time, amt, city))
        if int(amt) > 1000:
            invalid[i] = True

    for i, tx in enumerate(transactions):
        if invalid[i]:
            continue
        name, time, amt, city = tx.split(",")
        for oi, oname, otime, oamt, ocity in name_map[name]:
            if city != ocity and abs(int(time) - int(otime)) <= 60:
                invalid[i] = True
                invalid[oi] = True

    return [transactions[i] for i in range(len(transactions)) if invalid[i]]

