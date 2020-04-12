
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(l: ListNode):
    s = ''
    while l:
        s += f' -> {l.val}' if s else f'{l.val}'
        l = l.next
    print(s)


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

    print_list(og_sum_node)
    return og_sum_node







l1_2 = ListNode(3)
l1_1 = ListNode(4)
l1_1.next = l1_2
l1_0 = ListNode(2)
l1_0.next = l1_1

l2_2 = ListNode(4)
l2_1 = ListNode(6)
l2_1.next = l2_2
l2_0 = ListNode(5)
l2_0.next = l2_1

# Expect: 807
add_two_numbers(l1_0, l2_0)


l3_0 = ListNode(0)
l4_0 = ListNode(0)

# Expect: 0
add_two_numbers(l3_0, l4_0)


l5_0 = ListNode(5)
l6_0 = ListNode(5)

# Expect: 10
add_two_numbers(l5_0, l6_0)


l7_0 = ListNode(9)
l7_1 = ListNode(9)
l7_0.next = l7_1
l8_0 = ListNode(1)

# Expect: 100
add_two_numbers(l7_0, l8_0)
