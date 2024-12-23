from misc import TreeNode
from collections import deque

def minimumOperations(root: TreeNode) -> int:
    levels = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levels.append(level)

    res = 0

    for level in levels:
        index_map = {val: idx for idx, val in enumerate(level)}
        sorted_level = sorted(level)

        for i in range(len(level)):
            if sorted_level[i] != level[i]:
                res += 1
                idx = index_map[sorted_level[i]]
                index_map[level[i]] = idx
                level[idx] = level[i]

    return res

