def parrot_trouble(talking, hour):
    if hour >= 7 and hour <= 20:
        return False
    elif talking == True:
        return True
    else:
        return False