def string_match(a, b):
  x = 0
  y = 1
  tally = 0
  while y <= len(a)-1 and y <= len(b)-1:
    if a[x] + a[y] == b[x] + b[y]:
      tally = tally + 1
      x = x + 1
      y = y + 1
    else:
      x = x + 1
      y = y + 1
  return tally
