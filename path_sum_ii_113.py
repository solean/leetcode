from typing import List
from misc import TreeNode

def pathSum(root: TreeNode, targetSum: int) -> List[List[int]]:
    paths = []

    def dfs(node, sum_left, path):
        if not node: return None

        path.append(node.val)

        if not node.left and not node.right:
            if sum_left == node.val:
                paths.append(path.copy())
        else:
            dfs(node.left, sum_left - node.val, path)
            dfs(node.right, sum_left - node.val, path)

        path.pop()

    dfs(root, targetSum, [])
    return paths