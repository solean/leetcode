from typing import List

def minOperations(logs: List[str]) -> int:
    stack = []

    for cmd in logs:
        if cmd == "./":
            continue
        elif cmd == "../":
            if stack:
                stack.pop()
        else:
            stack.append(cmd)

    return len(stack)

