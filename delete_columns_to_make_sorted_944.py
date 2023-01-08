from typing import List

def min_deletion_size(strs: List[str]) -> int:
    num_deleted = 0

    for i in range(len(strs[0])):
        last_char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] < last_char:
                num_deleted += 1
                break
            last_char = strs[j][i]

    return num_deleted