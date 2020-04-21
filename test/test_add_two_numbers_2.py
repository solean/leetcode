from add_two_numbers_2 import add_two_numbers
from misc import ListNode, stringify_list
import unittest

class TestAddTwoNumbers(unittest.TestCase):

    def test_1(self):
        # Build list 1
        l1_2 = ListNode(3)
        l1_1 = ListNode(4)
        l1_1.next = l1_2
        l1_0 = ListNode(2)
        l1_0.next = l1_1

        # Build list 2
        l2_2 = ListNode(4)
        l2_1 = ListNode(6)
        l2_1.next = l2_2
        l2_0 = ListNode(5)
        l2_0.next = l2_1

        sum_list_node_0 = add_two_numbers(l1_0, l2_0)
        self.assertEqual(stringify_list(sum_list_node_0), '7 -> 0 -> 8')

    def test_2(self):
        l3_0 = ListNode(0)

        l4_0 = ListNode(0)

        sum_list_node_0 = add_two_numbers(l3_0, l4_0)
        self.assertEqual(stringify_list(sum_list_node_0), '0')

    def test_3(self):
        l5_0 = ListNode(5)
        l6_0 = ListNode(5)

        sum_list_node_0 = add_two_numbers(l5_0, l6_0)
        self.assertEqual(stringify_list(sum_list_node_0), '0 -> 1')

    def test_4(self):
        l7_0 = ListNode(9)
        l7_1 = ListNode(9)
        l7_0.next = l7_1
        l8_0 = ListNode(1)

        sum_list_node_0 = add_two_numbers(l7_0, l8_0)
        self.assertEqual(stringify_list(sum_list_node_0), '0 -> 0 -> 1')

