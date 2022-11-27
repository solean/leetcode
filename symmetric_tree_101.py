from misc import TreeNode

def is_symmetric(root: TreeNode) -> bool:
    if root is None:
        return True

    def dfs(left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        
        if left.val != right.val:
            return False
        else:
            return dfs(left.left, right.right) and dfs(left.right, right.left)
    
    return dfs(root.left, root.right)