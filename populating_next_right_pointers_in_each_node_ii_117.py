from collections import deque

def connect(root):
    q = deque([root])

    while q:
        level = []
        
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node)
                q.append(node.left)
                q.append(node.right)
            
        if level:
            for i in range(0, len(level) - 1):
                level[i].next = level[i + 1]
            level[-1].next = None
    
    return root
