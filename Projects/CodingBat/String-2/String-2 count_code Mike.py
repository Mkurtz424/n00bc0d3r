def count_code(str):
  x = 0
  y = 2
  z = 3
  codetally = 0
  while z < len(str):
    if str[x:y] == "co" and str[z] == "e":
      codetally = codetally + 1
      x = x + 1
      y = y + 1
      z = z + 1
    else:
      x = x + 1
      y = y + 1
      z = z + 1
  return codetally