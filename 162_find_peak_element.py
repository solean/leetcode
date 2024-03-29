from typing import List

def find_peak_element(nums: List[int]) -> int:
    n = len(nums)
    i = 0
    j = n - 1

    if n == 1:
        return 0
    elif nums[0] > nums[1]:
        return 0
    elif nums[j] > nums[j - 1]:
        return j

    while i <= j:
        mid = (i + j) // 2
        if mid - 1 >= 0 and mid + 1 < n:
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                j = mid
            elif nums[mid + 1] > nums[mid]:
                i = mid

    return -1

