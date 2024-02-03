
def is_palindrome(s: str) -> bool:
    if len(s) % 2 != 0:
        # splice out the middle char
        mid = len(s) // 2
        s = s[:mid] + s[mid+1:]
    
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True

def valid_palindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            # try "deleting" the char at i and check the inner string after i to j
            if is_palindrome(s[i+1:j+1]):
                return True
            # try "deleting" the char at j and the check the inner string from i to before j
            elif is_palindrome(s[i:j]):
                return True
            else:
                return False
        else:
            i += 1
            j -= 1
    
    return True
