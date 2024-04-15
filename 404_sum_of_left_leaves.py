from misc import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.left_leaves = 0

        def dfs(node, is_left):
            if not node:
                return

            if not node.left and not node.right and is_left:
                self.left_leaves += node.val

            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)
        return self.left_leaves

