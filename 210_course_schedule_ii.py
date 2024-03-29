from typing import List
from collections import defaultdict

def build_required_by_map(numCourses, prereqs):
    m = { i: [] for i in range(numCourses) }

    for p in prereqs:
        m[p[1]].append(p[0])

    return m

def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    order = []
    req_map = build_required_by_map(numCourses, prerequisites)

    indegrees = defaultdict(int)
    for node in req_map:
        for neighbor in req_map[node]:
            indegrees[neighbor] += 1
    
    # find course with no prereqs (has to be >= 1 starting course)
    no_incoming_edges = []
    for node in req_map:
        if indegrees[node] == 0:
            no_incoming_edges.append(node)
    
    while no_incoming_edges:
        node = no_incoming_edges.pop()
        order.append(node)

        for neighbor in req_map[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                no_incoming_edges.append(neighbor)

    if len(order) == len(req_map):
        return order
    else:
        # no possible order, or cycle detected
        return []