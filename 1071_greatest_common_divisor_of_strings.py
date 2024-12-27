
def gcdOfStrings(str1: str, str2: str) -> str:
    smallest_str = str1 if len(str1) < len(str2) else str2
    smallest_len = len(smallest_str)

    for i in range(smallest_len, 0, -1):
        if len(str1) % i == 0 and len(str2) % i == 0:
            divisor = smallest_str[:i]
            if divisor * int((len(str1) / i)) == str1 and divisor * int((len(str2) / i)) == str2:
                return divisor

    return ""

