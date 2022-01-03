from misc import ListNode

def middleNodeTwoPass(head: ListNode) -> ListNode:
    l = 0
    node = head
    while node:
        l += 1
        node = node.next

    i = 0
    while i < l // 2:
        i += 1
        head = head.next

    return head

# Two pointers, fast and slow. When fast gets to the end, slow is in the middle.
def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
