from misc import TreeNode

def isValidBST(root: TreeNode) -> bool:

    def dfs(node, left, right):
        if not node:
            return True

        if node.val > left and node.val < right:
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        else:
            return False

    return dfs(root, float('-inf'), float('inf'))
