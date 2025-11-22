
def minimumOperations(nums):
    return sum([1 for n in nums if n % 3 != 0])

