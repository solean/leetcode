
def makeGood(s: str) -> str:
    stack = []

    for ch in s:
        if stack and (ch != stack[-1] and ch.lower() == stack[-1].lower()):
            stack.pop()
        else:
            stack.append(ch)
    
    return ''.join(stack)
