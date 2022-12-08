from misc import TreeNode

def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:
    if not root1 or not root2:
        return False

    def dfs(node, leafs):
        if not node:
            return

        if not node.left and not node.right:
            leafs.append(node.val)

        dfs(node.left, leafs)
        dfs(node.right, leafs)

    leafs1 = []
    dfs(root1, leafs1)
    leafs2 = []
    dfs(root2, leafs2)

    return leafs1 == leafs2
