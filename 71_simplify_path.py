
def simplify_path(path: str) -> str:
    stack = []

    path_split = list(filter(None, path.split("/")))
    for section in path_split:
        if section == "..":
            if stack:
                stack.pop()
        elif section != ".":
            stack.append(section)

    new_path = "/" + "/".join(stack)
    return new_path

