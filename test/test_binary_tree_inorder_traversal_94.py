from binary_tree_inorder_traversal_94 import inorder_traversal
from misc import TreeNode
import unittest

class TestBinaryTreeInorderTraversal(unittest.TestCase):

    def test_1(self):
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
        self.assertEqual(inorder_traversal(tree), [1,3,2])

