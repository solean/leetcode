def calculate(s: str) -> int:
    s = s.strip()
    stack = []
    curr_num = ""
    op = "+"

    for i in range(len(s)):
        ch = s[i]

        if ch == " ":
            continue

        if ch.isdigit():
            curr_num += ch

        if not ch.isdigit() or i == len(s) - 1:
            curr_num = 0 if not curr_num else int(curr_num)
            if op == "-":
                stack.append(curr_num * -1)
            elif op == "+":
                stack.append(curr_num)
            elif op == "*":
                stack.append(stack.pop() * curr_num)
            elif op == "/":
                stack.append(int(stack.pop() / curr_num))
            
            op = ch
            curr_num = ""
    
    result = 0
    while stack:
        result += stack.pop()
    return result