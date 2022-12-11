from typing import List

def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    start_nums = []

    for n in nums:
        if n - 1 not in num_set:
            start_nums.append(n)

    max_seq_len = 0
    for n in start_nums:
        seq_len = 1
        while n + 1 in num_set:
            seq_len += 1
            n += 1
        max_seq_len = max(max_seq_len, seq_len)

    return max_seq_len