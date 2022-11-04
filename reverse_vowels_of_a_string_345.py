
def reverse_vowels(s: str) -> str:
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    arr = list(s)
    l = 0
    r = len(arr) - 1

    while l < r:
        if arr[l] in vowels and arr[r] in vowels:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        elif arr[l] not in vowels:
            l += 1
        else:
            r -= 1

    return ''.join(arr)
