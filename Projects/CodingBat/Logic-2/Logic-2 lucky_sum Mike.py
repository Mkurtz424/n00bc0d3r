def lucky_sum(a, b, c):
  x = 0
  stuff = [a,b,c]
  answer = 0
  while x<3 and stuff[x] != 13:
    answer = answer + stuff[x]
    x = x + 1
  return answer
