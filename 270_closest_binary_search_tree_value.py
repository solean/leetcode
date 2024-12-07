from misc import TreeNode

def closestValue(root: TreeNode, target: float) -> int:
    closest = float("inf")

    def dfs(node):
        nonlocal closest

        if not node:
            return

        diff_to_target = abs(target - node.val)
        diff_to_closest = abs(target - closest)

        if diff_to_target == diff_to_closest:
            closest = min(closest, node.val)
        elif diff_to_target < diff_to_closest:
            closest = node.val

        if target < node.val:
            dfs(node.left)
        else:
            dfs(node.right)


    dfs(root)
    return closest

