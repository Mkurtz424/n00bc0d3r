def end_other(a, b):
  alower = a.lower()
  blower = b.lower()
  if alower[-(len(b)):] == blower:
    return True
  elif blower[-(len(a)):] == alower:
    return True
  else:
    return False
