from sortedcontainers import SortedList

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.leaderboard = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            old_score = self.scores[playerId]
            new_score = old_score + score
            self.leaderboard.remove((-old_score, playerId))
            self.scores[playerId] += score
            self.leaderboard.add((-new_score, playerId))
        else:
            self.scores[playerId] = score
            self.leaderboard.add((-score, playerId))

    def top(self, K: int) -> int:
        return sum([-a for a, b in self.leaderboard[:K]])

    def reset(self, playerId: int) -> None:
        self.leaderboard.remove((-self.scores[playerId], playerId))
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId

