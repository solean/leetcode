from misc import TreeNode

def evaluateTree(root: TreeNode) -> bool:

    def dfs(node):
        if not node:
            return
        
        left = dfs(node.left)
        right = dfs(node.right)

        if node.val == 2:
            return left or right
        elif node.val == 3:
            return left and right
        else:
            return node.val


    return dfs(root)
