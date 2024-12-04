
def canMakeSubsequence(str1: str, str2: str) -> bool:
    if len(str2) > len(str1):
        return False

    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if (
            str1[i] == str2[j]
            or (str1[i] == "z" and str2[j] == "a")
            or ord(str1[i]) + 1 == ord(str2[j])
        ):
            j += 1

        i += 1

    return j == len(str2)

