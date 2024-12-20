from misc import TreeNode

def reverseOddLevels(root: TreeNode) -> TreeNode:

    def dfs(left, right, curr_level):
        if not left or not right:
            return

        if curr_level % 2 == 0:
            temp = left.val
            left.val = right.val
            right.val = temp

        dfs(left.left, right.right, curr_level + 1)
        dfs(left.right, right.left, curr_level + 1)


    dfs(root.left, root.right, 0)
    return root

