from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []

    for t in tokens:
        if t == '+':
            res = int(stack.pop()) + int(stack.pop())
        elif t == '-':
            second = stack.pop()
            first = stack.pop()
            res = first - second
        elif t == '*':
            res = int(stack.pop()) * int(stack.pop())
        elif t == '/':
            second = stack.pop()
            first = stack.pop()
            res = first / second
        else:
            res = t

        stack.append(res)

    return int(stack[0])
