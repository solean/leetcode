from misc import TreeNode

def smallestFromLeaf(root: TreeNode) -> str:
        smallest = None

        def dfs(node, s):
            nonlocal smallest

            if not node:
                return s

            s = chr(97 + node.val) + s

            if not node.left and not node.right:
                if not smallest or s < smallest:
                    smallest = s

            dfs(node.left, s)
            dfs(node.right, s)


        dfs(root, "")
        return smallest
 