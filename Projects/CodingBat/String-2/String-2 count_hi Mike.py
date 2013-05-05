def count_hi(str):
  tally = 0
  x = 0
  y = 1
  while y < len(str):
    if str[x] + str[y] == "hi":
      tally = tally + 1
      x = x + 1
      y = y + 1
    else:
      x = x + 1
      y = y + 1
  return tally
