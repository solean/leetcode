from collections import deque

def predictPartyVictory(senate: str) -> str:
    num_radiant = senate.count("R")
    num_dire = senate.count("D")

    ban_radiant = 0
    ban_dire = 0

    q = deque(list(senate))
    while q:
        curr = q.popleft()

        if not num_dire or not num_radiant:
            return "Radiant" if curr == "R" else "Dire"

        if curr == "R":
            if ban_radiant:
                ban_radiant -= 1
                num_radiant -= 1
            else:
                q.append("R")
                ban_dire += 1
        else:
            if ban_dire:
                ban_dire -= 1
                num_dire -= 1
            else:
                q.append("D")
                ban_radiant += 1

