from typing import List

# Sliding window solution
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    curr = set()

    for i in range(k + 1):
        if i < len(nums):
            n = nums[i]
            if n in curr:
                return True
            curr.add(n)

    i = 0
    j = k
    while j < len(nums):
        curr.remove(nums[i])

        if j < len(nums) - 1:
            if nums[j + 1] in curr:
                return True
            curr.add(nums[j + 1])

        i += 1
        j += 1

    return Fals


# Simpler hashmap solution
def containsNearbyDuplicateII(nums: List[int], k: int) -> bool:
    mp = defaultdict(int)

    for i in range(len(nums)):
        n = nums[i]

        if n in mp and abs(mp[n] - i) <= k:
            return True

        mp[n] = i

    return False

