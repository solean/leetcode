from same_tree_100 import is_same_tree
from misc import TreeNode
import unittest

class TestSameTree(unittest.TestCase):

    def test_same(self):
        tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
        tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

        self.assertTrue(is_same_tree(tree1, tree2))

    def test_diff_1(self):
        tree1 = TreeNode(1, TreeNode(2), None)
        tree2 = TreeNode(1, None, TreeNode(2))

        self.assertFalse(is_same_tree(tree1, tree2))
    
    def test_diff_2(self):
        tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
        tree2 = TreeNode(1, TreeNode(1), TreeNode(2))

        self.assertFalse(is_same_tree(tree1, tree2))

