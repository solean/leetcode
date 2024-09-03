
def getLucky(s: str, k: int) -> int:
    nums = ""
    for ch in s:
        nums += str(ord(ch.lower()) - 96)

    for _ in range(k):
        total = sum(int(ch) for ch in nums)
        nums = str(total)

    return int(nums)

