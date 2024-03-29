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


def flatten_no_extra_space(root: TreeNode) -> None:

    def dfs(node):
        if not node:
            return None
        
        left_tail = dfs(node.left)
        right_tail = dfs(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        tail = right_tail or left_tail or node
        return tail
    
    dfs(root)
