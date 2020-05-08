from typing import List

# O(n^2)
def three_sum(nums: List[int]) -> List[List[int]]:
    l = len(nums)
    nums = sorted(nums)
    three_sums = set()

    for i in range(l):
        opp = nums[i] * -1
        j = i + 1
        k = l - 1

        while j < k:
            sum_two = nums[j] + nums[k]
            if sum_two < opp:
                j += 1
            elif sum_two > opp:
                k -= 1
            else:
                three_sums.add((
                    nums[i],
                    nums[j],
                    nums[k]
                ))

                j += 1
                k -= 1

    return three_sums 

