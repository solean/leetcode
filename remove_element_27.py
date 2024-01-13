from typing import List

def remove_element(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

    return len(nums)

# New question requires elements to be "removed" in place (moved to end of array)
def remove_element_new(nums: List[int], val: int) -> int:
    i = 0
    j = len(nums)

    while i < j:
        if nums[i] == val:
            nums[i], nums[j - 1], nums[j - 1], nums[i]
            j -= 1
        else:
            i += 1

    return j

