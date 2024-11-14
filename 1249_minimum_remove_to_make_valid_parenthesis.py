
def minRemoveToMakeValid(s: str) -> str:
    stack = []
    to_remove = set()

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if not stack:
                to_remove.add(i)
            else:
                stack.pop()

    to_remove.update(stack)

    new_str = ""
    for i in range(0, len(s)):
        if i not in to_remove:
            new_str += s[i]

    return new_str

