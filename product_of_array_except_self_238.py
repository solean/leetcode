from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    le = len(nums)

    pre = [1 * nums[0]]
    for i in range(1, le - 1):
        pre.append(nums[i] * pre[i - 1])

    post = [1 for i in range(le)]
    post[le - 1] = nums[le - 1]
    for i in range(le - 2, -1, -1):
        post[i] = nums[i] * post[i + 1]

    res = [1 for i in range(le)]
    res[0] = post[1]
    res[le - 1] = pre[le - 2]
    for i in range(1, le - 1):
        res[i] = pre[i - 1] * post[i + 1]

    return res


print(product_except_self([-1,1,0,-3,3]))