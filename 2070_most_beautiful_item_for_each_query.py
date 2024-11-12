from typing import List

def maximumBeauty(items: List[List[int]], queries: List[int]) -> List[int]:
    ans = [0] * len(queries)

    items.sort(key=lambda x: (x[0], -x[1]))

    sorted_queries = [(i, price) for (i, price) in enumerate(queries)]
    sorted_queries.sort(key=lambda x: x[1])

    q, i = 0, 0
    max_so_far = 0
    while q < len(sorted_queries):
        query_index, query_price = sorted_queries[q]
        if i >= len(items) or items[i][0] > query_price:
            ans[query_index] = max_so_far
            q += 1
        else:
            max_so_far = max(max_so_far, items[i][1])
            i += 1

    return ans

