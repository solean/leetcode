from collections import defaultdict
from misc import TreeNode

class PathSumIII:
    def path_sum_iii(self, root: TreeNode, target: int) -> int:
        self.num_paths = 0
        self.map = defaultdict(int)
        self.map[target] = 1

        def dfs(node, curr):
            if not node: return

            curr += node.val
            self.num_paths += self.map[curr]
            self.map[curr + target] += 1

            dfs(node.left, curr)
            dfs(node.right, curr)

            self.map[curr + target] -= 1
        
        dfs(root, 0)
        return self.num_paths