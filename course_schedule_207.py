from typing import List
from collections import deque

def can_finish(numCourses: int, prereqs: List[List[int]]) -> bool:
    prereq_map = build_prereq_map(numCourses, prereqs)
    visiting = set()

    def dfs(course):
        if course in visiting:
            # cycle detected
            return False
        elif prereq_map[course] == []:
            return True

        visiting.add(course)

        for p in prereq_map[course]:
            if not dfs(p):
                return False

        visiting.remove(course)
        prereq_map[course] = []
        return True
            

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


def build_prereq_map(numCourses, prereqs):
    m = { i: [] for i in range(numCourses) }

    for p in prereqs:
        course = p[0]
        m[course].append(p[1])

    return m


def can_finish_bfs(numCourses: int, prereqs: List[List[int]]) -> bool:
    if not prereqs:
        return True

    prereq_map = defaultdict(set)
    indegree_map = defaultdict(set)
    for prereq, course in prereqs:
        prereq_map[prereq].add(course)
        indegree_map[course].add(prereq)

    q = deque()
    for i in range(numCourses):
        if not indegree_map[i]:
            q.append(i)

    num_visited = 0

    while q:
        node = q.popleft()
        num_visited += 1
        for nei in prereq_map[node]:
            if node in indegree_map[nei]:
                indegree_map[nei].remove(node)
            if not indegree_map[nei]:
                q.append(nei)
    
    return num_visited == numCourses
