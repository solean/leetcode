
def punishmentNumber(n: int) -> int:

    def can_partition(curr_sq, target):
        s = str(curr_sq)
        if not s and target == 0:
            return True

        for i in range(len(s)):
            l = s[:i + 1]
            r = s[i + 1:]
            if can_partition(r, target - int(l)):
                return True

        return False

    for i in range(1, n + 1):
        sq = i * i
        if can_partition(sq, i):
            res += curr_sq

    return res

