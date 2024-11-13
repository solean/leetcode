from typing import List
from misc import TreeNode

def verticalOrder(root: TreeNode) -> List[List[int]]:
    levels = defaultdict(list)
    min_level = float("inf")
    max_level = float("-inf")

    if not root:
        return []

    def dfs(node, level, depth):
        nonlocal min_level
        nonlocal max_level

        min_level = min(min_level, level)
        max_level = min(max_level, level)

        levels[level].append((node.val, depth))

        if node.left:
            dfs(node.left, level - 1, depth + 1)
        if node.right:
            dfs(node.right, level + 1, depth + 1)


    dfs(root, 0, 0)

    vertical_order = []
    for i in range(min_level, max_level + 1):
        level = levels[i]
        level.sort(key=lambda x: x[1])
        vertical_order.append([val for (val, depth) in level])

    return vertical_order

