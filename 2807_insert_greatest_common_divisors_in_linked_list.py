import math
from misc import ListNode

def insertGreatestCommonDivisors(head: ListNode) -> ListNode:
    node = head
    while node and node.next:
        gcd = math.gcd(node.val, node.next.val)
        gcd_node = ListNode(val=gcd)

        nxt = node.next
        node.next = gcd_node
        gcd_node.next = nxt
        node = nxt

    return head

