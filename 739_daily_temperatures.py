from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    l = len(temperatures)
    res = [0] * l
    stack = [
        # [temp, index]
    ]
    
    for i in range(l):
        t = temperatures[i]
        
        while stack and t > stack[-1][0]:
            s = stack.pop()
            res[s[1]] = i - s[1]
            
        stack.append([t, i])
        
    return res