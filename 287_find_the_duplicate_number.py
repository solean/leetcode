from typing import List

def find_duplicate(nums: List[int]) -> int:
    slow = 0
    fast = 0

    while slow != fast or slow == 0:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow2 = 0
    while slow != slow2 or slow2 == 0:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow