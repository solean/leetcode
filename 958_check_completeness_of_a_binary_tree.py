from misc import TreeNode
from collections import deque

def isCompleteTree(root: TreeNode) -> bool:
    levels = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val if node else None)
            if node:
                q.append(node.left)
                q.append(node.right)

        levels.append(level)

    # the last level atp will be all None (empty leafs)
    levels.pop()

    # check that all levels except last one are full
    for i in range(0, len(levels) - 1):
        level = levels[i]
        for j in range(len(level)):
            if level[j] is None:
                return False

    last_level = levels[-1]
    last_num_index = None
    for i in range(len(last_level) - 1, -1, -1):
        if last_level[i] is not None:
            last_num_index = i
            break

    # check that all leafs are as far left as possible
    for i in range(len(last_level)):
        if last_level[i] is None and i < last_num_index:
            return False

    return True

