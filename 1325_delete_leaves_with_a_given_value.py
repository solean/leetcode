from misc import TreeNode

def removeLeafNodes(root: TreeNode, target: int) -> TreeNode:
    def dfs(node):
        if not node:
            return

        node.left = dfs(node.left)
        node.right = dfs(node.right)
        
        if node.val == target and not node.left and not node.right:
            return None
        
        return node


    return dfs(root)
