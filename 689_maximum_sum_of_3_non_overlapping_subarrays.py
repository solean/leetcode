from typing import List

def maxSumOfThreeSubarrays(nums: List[int], k: int) -> List[int]:
    k_sums = [sum(nums[:k])]
    for i in range(k, len(nums)):
        k_sums.append(k_sums[-1] + nums[i] - nums[i - k])

    dp = {}

    def get_max_sum(i, count):
        if count == 3 or i > len(nums) - k:
            return 0
        if (i, count) in dp:
            return dp[(i, count)]

        include = k_sums[i] + get_max_sum(i + k, count + 1)
        skip = get_max_sum(i + 1, count)

        dp[(i, count)] = max(include, skip)
        return max(include, skip)

    i = 0
    indices = []

    while i <= len(nums) - k and len(indices) < 3:
        include = k_sums[i] + get_max_sum(i + k, len(indices) + 1)
        skip = get_max_sum(i + 1, len(indices))

        if include >= skip:
            indices.append(i)
            i += k
        else:
            i += 1

    return indices

