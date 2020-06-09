from remove_duplicates_from_sorted_list_83 import delete_duplicates
from misc import ListNode, stringify_list
import unittest

class TestRemoveDuplicatesFromSortedList(unittest.TestCase):

    def test_1(self):
        l = ListNode(1, ListNode(1, ListNode(2)))
        trimmed = delete_duplicates(l)
        expected = '1 -> 2'
        self.assertEqual(stringify_list(trimmed), expected)

    def test_2(self):
        l = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        trimmed = delete_duplicates(l)
        expected = '1 -> 2 -> 3'
        self.assertEqual(stringify_list(trimmed), expected)

    def test_3(self):
        l = ListNode(1, ListNode(1, ListNode(1)))
        trimmed = delete_duplicates(l)
        expected = '1'
        self.assertEqual(stringify_list(trimmed), expected)

    def test_4(self):
        l = ListNode(1, ListNode(1, ListNode(1, ListNode(2))))
        trimmed = delete_duplicates(l)
        expected = '1 -> 2'
        self.assertEqual(stringify_list(trimmed), expected)

