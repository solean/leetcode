from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    group = dict()

    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in group:
            group[sorted_s] = group[sorted_s] + [s]
        else:
            group[sorted_s] = [s]


    l = [group[key] for key in group]
    return l

