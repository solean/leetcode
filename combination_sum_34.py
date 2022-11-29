from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    combos = []

    def dfs(i, curr, total):
        if total == target:
            combos.append(curr.copy())
            return
        elif i >= len(candidates) or total > target:
            return

        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])

        # backtrack
        curr.pop()
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return combos

