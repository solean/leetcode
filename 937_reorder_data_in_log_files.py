from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:
    letter_logs = []
    digit_logs = []

    for log in logs:
        split_log = log.split(" ")
        if split_log[1].isalpha():
            letter_logs.append((split_log[0], " ".join(split_log[1:])))
        else:
            digit_logs.append(log)

    res = []

    letter_logs.sort(key=lambda x: (x[1], x[0]))
    for letter_log in letter_logs:
        res.append(letter_log[0] + " " + letter_log[1])

    for digit_log in digit_logs:
        res.append(digit_log)

    return res

