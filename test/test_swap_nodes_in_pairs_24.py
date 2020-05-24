from swap_nodes_in_pairs_24 import swap_pairs
from misc import ListNode, stringify_list
import unittest

class TestSwapNodesInPairs(unittest.TestCase):

    def test_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        head = swap_pairs(head)
        s = stringify_list(head)
        self.assertEqual(s, "2 -> 1 -> 4 -> 3")

    def test_2(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        head = swap_pairs(head)
        s = stringify_list(head)
        self.assertEqual(s, "2 -> 1 -> 3")

    def test_3(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        head = swap_pairs(head)
        s = stringify_list(head)
        self.assertEqual(s, "2 -> 1 -> 4 -> 3 -> 6 -> 5")

    def test_4(self):
        head = ListNode(1, ListNode(2))
        head = swap_pairs(head)
        s = stringify_list(head)
        self.assertEqual(s, "2 -> 1")

