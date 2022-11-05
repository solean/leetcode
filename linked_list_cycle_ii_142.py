from misc import ListNode

def detect_cycle_2(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None

    cycle = False
    turtle = head
    hare = head

    while turtle and hare and hare.next:
        turtle = turtle.next
        hare = hare.next.next

        if turtle == hare:
            cycle = True
            break

    if not cycle:
        return None

    turtle = head
    while turtle != hare:
        turtle = turtle.next
        hare = hare.next

    return turtle
