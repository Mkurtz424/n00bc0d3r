def lone_sum(a, b, c):
  if a != b:
    if a!= c:
      if b!= c:
        return a+b+c
      else:
        return a
    else:
      return b
  else:
    if b!=c:
      return c
    else:
      return 0
