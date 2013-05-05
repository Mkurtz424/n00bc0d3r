def double_char(str):
  answer = ""
  x = 0
  while x < len(str):
    answer = answer + str[x] * 2
    x = x + 1
  return answer