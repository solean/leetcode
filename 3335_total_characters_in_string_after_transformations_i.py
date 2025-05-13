
def lengthAfterTransformations(s: str, t: int) -> int:
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 97] += 1

    for i in range(t):
        num_z = counts[25]

        for j in range(25, 0, -1):
            counts[j] += counts[j - 1]
            counts[j - 1] = 0

        if num_z:
            counts[0] += num_z
            counts[1] += num_z
            counts[25] -= num_z


    MOD = 10**9 + 7
    return sum(counts) % MOD

