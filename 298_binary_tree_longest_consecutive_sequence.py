from misc import TreeNode

def longestConsecutive(root: TreeNode) -> int:
    maxpath = 0

    def dfs(node, parentval, currpath):
        nonlocal maxpath

        if not node:
            return

        if parentval is None or node.val == parentval + 1:
            currpath += 1
            maxpath = max(maxpath, currpath)
        else:
            currpath = 1

        dfs(node.left, node.val, currpath)
        dfs(node.right, node.val, currpath)


    dfs(root, None, 0)

    return maxpath

