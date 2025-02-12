from typing import List

def maximumSum(self, nums: List[int]) -> int:
    n = len(nums)

    def get_digits_sum(num):
        return sum(list(map(lambda x: int(x), list(str(num)))))


    nums = [(get_digits_sum(x), x) for x in nums]
    nums.sort()

    max_sum = float("-inf")
    for i in range(1, n):
        if nums[i][0] == nums[i - 1][0]:
            max_sum = max(max_sum, nums[i][1] + nums[i - 1][1])

    return -1 if max_sum == float("-inf") else max_sum

