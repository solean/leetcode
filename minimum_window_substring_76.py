from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    counts = Counter(t)
    shortest_window = ""
    i = 0

    chars_satisfied = 0
    curr_window_counts = defaultdict(int)

    for j in range(len(s)):
        curr_window_counts[s[j]] += 1

        if s[j] in counts and curr_window_counts[s[j]] == counts[s[j]]:
            chars_satisfied += 1

        
        if chars_satisfied == len(counts):
            while i <= j:
                if not shortest_window or j - i + 1 < len(shortest_window):
                    shortest_window = s[i:j+1]
                
                curr_window_counts[s[i]] -= 1
                if s[i] in counts and curr_window_counts[s[i]] < counts[s[i]]:
                    chars_satisfied -= 1
                
                i += 1

                if chars_satisfied != len(counts):
                    break
    
    return shortest_window