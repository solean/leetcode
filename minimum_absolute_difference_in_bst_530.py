from misc import TreeNode

def getMinimumDifference(root: TreeNode) -> int:
    min_diff = 999999999
    vals = []

    def dfs(node):
        if not node:
            return

        nonlocal min_diff

        dfs(node.left)
        vals.append(node.val)
        if len(vals) > 1:
            min_diff = min(min_diff, abs(vals[-1] - vals[-2]))
        dfs(node.right)

    dfs(root)

    return min_diff
