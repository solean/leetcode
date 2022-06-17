from typing import List

def generate_parentheses(n: int) -> List[str]:
    stack = []
    res = []

    def recurse(num_open, num_closed):
        if num_open == num_closed == n:
            res.append(''.join(stack))
            return

        if num_open < n:
            stack.append('(')
            recurse(num_open + 1, num_closed)
            stack.pop()

        if num_closed < num_open:
            stack.append(')')
            recurse(num_open, num_closed + 1)
            stack.pop()

    recurse(0, 0)
    return res
