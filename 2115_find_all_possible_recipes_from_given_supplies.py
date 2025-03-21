from typing import List
from collections import defaultdict

def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    recipe_set = set(recipes)
    adj = defaultdict(list)
    indegrees = {recipe: 0 for recipe in recipes}

    for i, ings in enumerate(ingredients):
        for ing in ings:
            adj[ing].append(recipes[i])
            indegrees[recipes[i]] += 1

    res = 0
    q = deque(supplies)

    while q:
        node = q.popleft()

        if node in recipe_set:
            res.append(node)

        for recipe in adj[node]:
            indegrees[recipe] -= 1
            if indegrees[recipe] == 0:
                q.append(recipe)

    return res

