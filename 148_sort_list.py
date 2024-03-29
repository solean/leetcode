from misc import ListNode

def get_mid(head: ListNode) -> ListNode:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left: ListNode, right: ListNode) -> ListNode:
    node = ListNode()
    head = node

    while left and right:
        if left.val < right.val:
            node.next = left
            left = left.next
        else:
            node.next = right
            right = right.next
        node = node.next

    if left:
        node.next = left
    if right:
        node.next = right

    return head.next


def sort(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    left = head
    right = get_mid(head)
    temp = right.next
    right.next = None
    right = temp

    left = sort(left)
    right = sort(right)

    merged = merge(left, right)
    return merged