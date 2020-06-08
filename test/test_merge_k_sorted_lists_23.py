from merge_k_sorted_lists_23 import merge_k_lists
from misc import ListNode, stringify_list
import unittest

class TestMergeKSortedLists(unittest.TestCase):

    def test_1(self):
        k = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6))
        ]
        expected = '1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6'
        merged = merge_k_lists(k)
        self.assertEqual(stringify_list(merged), expected)

    def test_2(self):
        k = [
            None,
            None
        ]
        expected = ''
        merged = merge_k_lists(k)
        self.assertEqual(stringify_list(merged), expected)

    def test_3(self):
        k = [
            ListNode(1),
            ListNode(0)
        ]
        expected = '0 -> 1'
        merged = merge_k_lists(k)
        self.assertEqual(stringify_list(merged), expected)

    def test_4(self):
        k = [
            ListNode(1, ListNode(2, ListNode(2))),
            ListNode(1, ListNode(1, ListNode(2)))
        ]
        expected = '1 -> 1 -> 1 -> 2 -> 2 -> 2'
        merged = merge_k_lists(k)
        self.assertEqual(stringify_list(merged), expected)

