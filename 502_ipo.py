from typing import List
import heapq

# My initial, non-optimal solution. O(k * n log(n))
def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    profit_max_heap = []
    for i in range(len(profits)):
        heapq.heappush(profit_max_heap, (-profits[i], i))
    
    projects_completed = 0
    while projects_completed < k:
        temp = []
        found_project = False
        
        while not found_project and profit_max_heap:
            neg_profit, i = heapq.heappop(profit_max_heap)
            if capital[i] <= w:
                w += profits[i]
                projects_completed += 1
                found_project = True
            else:
                temp.append((neg_profit, i))
        
        if not found_project and not profit_max_heap:
            break
        else:
            for t in temp:
                heapq.heappush(profit_max_heap, t)
    
    return w


# Optimal O(n log(n)) solution
def findMaximizedCapitalOptimal(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    profit_max_heap = []
    capital_min_heap = []
    for i in range(len(profits)):
        if capital[i] <= w:
            heapq.heappush(profit_max_heap, (-profits[i], i))
        else:
            heapq.heappush(capital_min_heap, (capital[i], i))
    
    while k:
        while capital_min_heap:
            c, i = capital_min_heap[0]
            if c <= w:
                heapq.heappop(capital_min_heap)
                heapq.heappush(profit_max_heap, (-profits[i], i))
            else:
                break
        
        if not profit_max_heap:
            break

        neg_profit, i = heapq.heappop(profit_max_heap)
        w += profits[i]
        k -= 1

    return w
