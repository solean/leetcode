from misc import TreeNode

def sumNumbers(root: TreeNode) -> int:
    path_sums = 0

    def dfs(node, curr_path):
        nonlocal paths_sum

        if not node:
            return
        
        curr_path.append(node.val)
        
        if not node.left and not node.right:
            path_sums += int(''.join(map(str, curr_path)))
        
        dfs(node.left, curr_path)
        dfs(node.right, curr_path)

        if curr_path:
            curr_path.pop()
    
    dfs(root, [])
    return path_sums
