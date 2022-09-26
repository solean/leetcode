from typing import List

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
