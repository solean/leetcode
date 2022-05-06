from misc import TreeNode

def isBalanced(root: TreeNode) -> bool:

    def dfs(node: TreeNode) -> [bool, int]:
        if not node:
            return [True, 0]

        left = dfs(node.left)
        right = dfs(node.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]
