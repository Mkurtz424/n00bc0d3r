def sum67(nums):
  list = nums
  x = 0
  total = 0
  while x < len(list):
    if list[x] == 6:
      ignore = True
      while ignore == True:
        x = x + 1
        if x >= len(list):
          return total
        if list[x] == 7:
          ignore = False
          x = x + 1
          if x >= len(list):
            return total
    if list[x] != 6:
      total = total + list[x]
      x = x + 1
      if x >= len(list):
        return total
  return total