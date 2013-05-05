def near_ten(num):
  if num == 0:
    return True
  elif num%10 <=2 or num%10 >=8:
    return True
  else:
    return False
