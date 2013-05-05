def front_back(str):
    if len(str) <= 1:
        print str
    elif len(str) == 2:
        print (str[1] + str[0])
    else:
        n = len(str)
        print (str[n-1] + str[1:n-1] +  str[0])