from misc import TreeNode

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diam = 0
        self.dfs(root)
        return self.diam
        
    def dfs(self, node):
        if not node:
            return 0

        left = 0
        if node.left:
            left = 1 + self.dfs(node.left)

        right = 0
        if node.right:
            right = 1 + self.dfs(node.right)

        d = left + right
        if d > self.diam:
            self.diam = d
        
        return max(left, right)
        
