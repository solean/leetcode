def moveZeroes3(nums):
    n = len(nums)
    result = [0] * n

    r = 0
    for i in range(n):
        if nums[i] != 0:
            result[r] = nums[i]
            r += 1

    print(result)

    for j in range(n):
        nums[j] = result[j]

def moveZeroes2(nums):
    last_non_zero_found = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found] = nums[i]
            last_non_zero_found += 1

    for i in range(last_non_zero_found, len(nums)):
        nums[i] = 0

def moveZeroes(nums):
    last = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[last] = nums[last], nums[i]
            last += 1


# Expect: [1, 3, 12, 0, 0]
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)