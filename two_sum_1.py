from typing import List
import unittest

# Only works if nums is sorted
def twoSumAlreadySorted(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        n = nums[i]

        if n >= target:
            break

        for j in range(i+1, len(nums)):
            print(f'{n} + {nums[j]}')
            if n + nums[j] == target:
                return [i, j]
            elif nums[j] >= target:
                break

    return None


def twoSumTwoPass(nums: List[int], target: int) -> List[int]:
    d = {}

    # store index
    for i in range(0, len(nums)):
        d[nums[i]] = i

    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in d and d[diff] != i:
            return [i, d[diff]]

    return None


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}

    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in d:
            return [d[diff], i]
        else:
            d[nums[i]] = i

    return None



class TestTwoSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(twoSum([1, 2, 7, 11, 15], 9), [1, 2])

    def test_2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])


if __name__ == '__main__':
    unittest.main()
