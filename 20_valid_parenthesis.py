
def is_valid(s: str) -> bool:
    if not s or s == '':
        return True

    to_close = ''

    for ch in s:
        if len(to_close) == 0:
            if is_closing(ch):
                return False
            else:
                to_close += get_closing(ch)
                continue

        if ch == to_close[-1]:
            to_close = to_close[:-1]
        elif is_closing(ch):
            return False
        else:
            to_close += get_closing(ch)

    return len(to_close) == 0

def get_closing(ch: str) -> str:
    if ch == '(':
        return ')'
    elif ch == '[':
        return ']'
    elif ch == '{':
        return '}'

def is_closing(ch: str) -> bool:
    return ch == ')' or ch == ']' or ch == '}'
