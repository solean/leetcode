from collections import deque
from typing import List

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    q = deque([startGene])
    visited = set()
    num_muts = 0

    while q:
        for _ in range(len(q)):
            gene = q.popleft()

            if gene == endGene:
                return num_muts

            for valid_gene in bank:
                num_diffs = 0
                for ch1, ch2 in zip(gene, valid_gene):
                    if ch1 != ch2:
                        num_diffs += 1
                        if num_diffs > 1:
                            break

                if num_diffs == 1 and valid_gene not in visited:
                    q.append(valid_gene)
                    visited.add(valid_gene)

        num_muts += 1

    return -1

