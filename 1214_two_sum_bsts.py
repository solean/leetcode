from misc import TreeNode

def twoSumBSTs(root1: TreeNode, root2: TreeNode, target: int) -> bool:
    d = {}

    def dfs(node, isTree1):
        if not node:
            return

        if not isTree1 and target - node.val in d:
            return True

        if isTree1:
            d[node.val] = True

        return dfs(node.left, isTree1) or dfs(node.right, isTree1)

    dfs(root1, True)
    return dfs(root2, False)

