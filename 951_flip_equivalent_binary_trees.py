from misc import TreeNode

def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:

    def dfs(node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return (dfs(node1.left, node2.left) and dfs(node1.right, node2.right)) or (dfs(node1.left, node2.right) and dfs(node1.right, node2.left))


    return dfs(root1, root2)

