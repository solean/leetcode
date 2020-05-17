from remove_nth_node_from_end_of_list_19 import remove_nth_from_end
from misc import ListNode, stringify_list
import unittest

class TestRemoveNthNodeFromEndOfList(unittest.TestCase):

    def test_1(self):
        l4 = ListNode(5)
        l3 = ListNode(4)
        l3.next = l4
        l2 = ListNode(3)
        l2.next = l3
        l1 = ListNode(2)
        l1.next = l2
        l0 = ListNode(1)
        l0.next = l1

        new_l = remove_nth_from_end(l0, 2)
        str_new_l = stringify_list(new_l)
        self.assertEqual(str_new_l, '1 -> 2 -> 3 -> 5')
    
    def test_2(self):
        l1 = ListNode(2)
        l0 = ListNode(1)
        l0.next = l1

        new_l = remove_nth_from_end(l0, 2)
        str_new_l = stringify_list(new_l)
        self.assertEqual(str_new_l, '2')

    def test_single(self):
        l0 = ListNode(1)

        new_l = remove_nth_from_end(l0, 1)
        str_new_l = stringify_list(new_l)
        self.assertEqual(str_new_l, '')

