from misc import TreeNode

def str2tree(s: str) -> TreeNode:
    if not s:
        return None
    
    def getnum(s, index):
        is_neg = False
        if s[index] == "-":
            is_neg = True
            index += 1
        
        n_str = ""
        while index < len(s) and s[index].isdigit():
            n_str += s[index]
            index += 1
        
        return (int(n_str) if not is_neg else -int(n_str)), index

    root = TreeNode(val=s[0])
    stack = [root]
    i = 0
    while i < len(s):
        node = stack.pop()
        if s[i].isdigit() or s[i] == "-":
            val, i = getnum(s, i)
            node.val = val
            if i < len(s) and s[i] == "(":
                stack.append(node)
                node.left = TreeNode()
                stack.append(node.left)
        elif node.left and s[i] == "(":
            stack.append(node)
            node.right = TreeNode()
            stack.append(node.right)

        i += 1
    
    return stack.pop() if stack else root

