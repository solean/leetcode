
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def stringify_list(l: ListNode) -> str:
    s = ''
    while l:
        s += f' -> {l.val}' if s else f'{l.val}'
        l = l.next
    return s

