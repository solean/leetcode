def int_to_roman(num: int) -> str:
    m = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    s = ""
    for n in reversed(list(m.keys())):
        while num >= n:
            s += m[n]
            num -= n

    return s
