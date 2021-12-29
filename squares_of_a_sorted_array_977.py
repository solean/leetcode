    
def sortedSquares(nums):
    result = [None] * len(nums)

    i = 0
    j = len(nums) - 1
    for r in range(len(nums) - 1, -1, -1):
        if abs(nums[i]) > abs(nums[j]):
            result[r] = nums[i] ** 2
            i += 1
        else:
            result[r] = nums[j] ** 2
            j -= 1
    
    return result


ans = sortedSquares([-4, -1, 0, 3, 10])
print(ans)