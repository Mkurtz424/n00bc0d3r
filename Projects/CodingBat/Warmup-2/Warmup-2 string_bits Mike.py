def string_bits(str):
    x = 0
    y = ""
    while x < len(str):
        y = y + str[x]
        x=x+2
    return y