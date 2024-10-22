from misc import TreeNode
from collections import deque
import heapq

def kthLargestLevelSum(root: TreeNode, k: int) -> int:
    q = deque()
    q.append(root)
    levels = []

    while q:
        level_sum = 0

        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        levels.append(level_sum)

    return levels[k - 1] if k <= len(levels) else -1


def kthLargestLevelSumOptimized(root: TreeNode, k: int) -> int:
    q = deque()
    q.append(root)
    min_heap = []

    while q:
        level_sum = 0

        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        heapq.heappush(min_heap, level_sum)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0] if k <= len(min_heap) else -1

