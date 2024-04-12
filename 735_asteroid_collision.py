from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = [asteroids.pop(0)]

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if abs(a) > abs(stack[-1]):
                stack.pop()
            elif abs(stack[-1]) > abs(a):
                a = 0
            else:
                stack.pop()
                a = 0

        if a:
            stack.append(a)

    return stack
