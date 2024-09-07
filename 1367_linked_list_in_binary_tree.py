from misc import ListNode, TreeNode

def isSubPath(head: ListNode, root: TreeNode) -> bool:

    def dfs(node: TreeNode, curr: ListNode):
        if not curr:
            return True
        if not node:
            return False

        if node.val == curr.val:
            if not curr.next:
                return True

            return dfs(node.left, curr.next) or dfs(node.right, curr.next)
        else:
            return False

    def search(node):
        if not node:
            return False

        if dfs(node, head):
            return True
        else:
            return search(node.left) or search(node.right)


    return search(root)

