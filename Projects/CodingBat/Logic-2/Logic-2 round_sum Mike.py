def round10(num):
  x = num / 10
  rem = num - (10*x)
  if rem >=5:
    num = (x * 10)+10
    return num
  else:
    num = (x * 10)
    return num
def round_sum(a, b, c):
  roundsum = round10(a) + round10(b) + round10(c)
  return roundsum
  
