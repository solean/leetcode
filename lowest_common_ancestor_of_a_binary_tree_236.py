from misc import TreeNode

def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

    def dfs(node):
        if not node:
            return None
        
        if node == p or node == q:
            return node
        
        left = dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return node
        else:
            return left or right

    return dfs(root)
