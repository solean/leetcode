from misc import TreeNode

def flatten(root: TreeNode) -> None:
    traversal = []

    def dfs(node):
        nonlocal traversal

        if not node:
            return
        
        traversal.append(node)
        dfs(node.left)
        dfs(node.right)
    
    for i in range(len(traversal) - 1):
        node = traversal[i]
        node.left = None
        node.right = traversal[i + 1]
