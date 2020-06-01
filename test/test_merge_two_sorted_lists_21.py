from merge_two_sorted_lists_21 import merge_two_lists
from misc import ListNode, stringify_list
import unittest

class TestMergeTwoSortedLists(unittest.TestCase):

    def test_1(self):
        l1_2 = ListNode(4)
        l1_1 = ListNode(2)
        l1_1.next = l1_2
        l1_0 = ListNode(1)
        l1_0.next = l1_1

        l2_2 = ListNode(4)
        l2_1 = ListNode(3)
        l2_1.next = l2_2
        l2_0 = ListNode(1)
        l2_0.next = l2_1

        expected = '1 -> 1 -> 2 -> 3 -> 4 -> 4'
        merged = merge_two_lists(l1_0, l2_0)
        self.assertEqual(stringify_list(merged), expected)

    def test_2(self):
        l1 = None
        l2 = ListNode(0)

        expected = '0'
        merged = merge_two_lists(l1, l2)
        self.assertEqual(stringify_list(merged), expected)

