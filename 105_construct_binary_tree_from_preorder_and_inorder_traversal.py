from misc import TreeNode

def buildTree(preorder, inorder) -> TreeNode:
    if not preorder or not inorder:
        return None

    rootVal = preorder[0]
    root = TreeNode(val=rootVal)
    i = inorder.index(rootVal)
    root.left = buildTree(preorder[1:i+1], inorder[:i])
    root.right = buildTree(preorder[i+1:], inorder[i+1:])
    return root
