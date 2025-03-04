
def decodeString(s: str) -> str:
    stack = []

    for ch in s:
        if ch == "]":
            encoded = ""
            while stack[-1] != "[":
                encoded = stack.pop() + encoded
            stack.pop()

            n_str = ""
            while stack and stack[-1].isdigit():
                n_str = stack.pop() + n_str

            stack.append(int(n_str) * encoded)
        else:
            stack.append(ch)

    return "".join(stack)

