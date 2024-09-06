from typing import List
from misc import ListNode

def modifiedList(nums: List[int], head: ListNode) -> ListNode:
    nums_set = set(nums)

    prev = None
    node = head
    while node:
        if node.val in nums_set:
            if prev:
                prev.next = node.next
            if node == head:
                head = node.next
        else:
            prev = node

        node = node.next

    return head

