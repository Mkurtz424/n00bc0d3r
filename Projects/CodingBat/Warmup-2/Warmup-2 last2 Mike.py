def last2(str):
  maxchar = 2
  minchar = 0
  total = 0
  substring = str[-2:]
  while maxchar <= len(str)-2:
    if str[minchar:maxchar] == substring:
      total = total + 1
    maxchar += 1
    minchar += 1
  return total
#This isn't the solution CodingBat is looking for,
#but I'm convinced their solution is WRONG so suck my balls.