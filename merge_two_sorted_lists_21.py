from misc import ListNode

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    i = l1
    j = l2
    curr_node = None
    og_node = None

    while i or j:
        if i is None:
            if curr_node is None:
                return j
            else:
                curr_node.next = j
                break
        elif j is None:
            if curr_node is None:
                return i
            else:
                curr_node.next = i
                break

        if i.val <= j.val:
            if curr_node is None:
                curr_node = i
                og_node = curr_node
            else:
                curr_node.next = i
                curr_node = curr_node.next
            i = i.next
        else:
            if curr_node is None:
                curr_node = j
                og_node = curr_node
            else:
                curr_node.next = j
                curr_node = curr_node.next
            j = j.next

    return og_node

