
def isBadVersion(n, bad):
    return n >= bad


def first_bad_version(n, bad):
    if n == 1:
        return 1

    i = 1
    j = n

    while i < j:
        mid = i + ((j - i) // 2)

        if not isBadVersion(mid, bad) and isBadVersion(mid + 1, bad):
            return mid + 1
        elif isBadVersion(mid, bad):
            if mid == 1:
                return 1
            else:
                j = mid
        else:
            i = mid

    return None

# ans = first_bad_version(2126753390, 1702766719)
# ans = first_bad_version(27, 21)
# print(ans)