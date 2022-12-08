from misc import TreeNode

class Solution:
    def range_sum_bst(self, root: TreeNode, low: int, high: int) -> int:
        self.total = 0

        def dfs(node):
            if not node:
                return

            if low <= node.val <= high:
                self.total += node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.total
