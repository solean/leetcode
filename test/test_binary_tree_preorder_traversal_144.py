from binary_tree_preorder_traversal_144 import preorder_traversal
from misc import TreeNode
import unittest

class TestBinaryTreePreorderTraversal(unittest.TestCase):

    def test_1(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
        expected = [1, 2, 3]
        self.assertCountEqual(preorder_traversal(root), expected)

