from misc import ListNode

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    og_sum_node = None
    curr_sum_node = None
    carry = False

    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        sum_val = None

        if l1_val != None and l2_val != None:
            summed = l1_val + l2_val
            if carry:
                summed += 1

            if summed > 9:
                carry = True
                # last digit only
                sum_val = summed % 10
            else:
                carry = False
                sum_val = summed

        if sum_val != None:
            sum_node = ListNode(sum_val)
            if curr_sum_node:
                curr_sum_node.next = sum_node
                curr_sum_node = sum_node
            else:
                og_sum_node = sum_node
                curr_sum_node = sum_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        curr_sum_node.next = ListNode(1)

    return og_sum_node

