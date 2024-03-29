from typing import List
from misc import TreeNode

class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sorted_array_to_bst(nums[:mid])
        node.right = self.sorted_array_to_bst(nums[mid+1:])
        return node
