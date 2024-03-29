from typing import List

def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    visited = set()

    def dfs(room):
        if room not in visited:
            visited.add(room)

            keys_in_room = rooms[room]
            for k in keys_in_room:
                dfs(k)

    dfs(0)

    return len(visited) == len(rooms)