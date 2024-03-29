from collections import defaultdict

def getHint(secret: str, guess: str) -> str:
    n = len(secret)
    a, b = 0, 0
    secret_map = defaultdict(int)
    guess_map = defaultdict(int)

    for i in range(n):
        if secret[i] == guess[i]:
            a += 1
        else:
            secret_map[secret[i]] += 1
            guess_map[guess[i]] += 1
        
    
    for key in guess_map:
        if key in secret_map:
            b += min(secret_map[key], guess_map[key])

    return f"{a}A{b}B"
    