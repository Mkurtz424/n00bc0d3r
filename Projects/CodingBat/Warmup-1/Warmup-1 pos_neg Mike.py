def pos_neg(a, b, negative):
    if negative == True:
        if a < 0 and b < 0:
            return True
        else:
            return False
    elif a >= 0 and b < 0:
        return True
    elif a < 0 and b >=0:
        return True
    else:
        return False
    
