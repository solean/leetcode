from typing import List

def numberOfBeams(bank: List[str]) -> int:
    num_devices = [row.count("1") for row in bank if row.count("1")]
    beams = 0

    for i in range(len(num_devices) - 1):
        beams += num_devices[i] * num_devices[i + 1]

    return beams

