def has22(nums):
  x = 0
  y = 1
  list = nums
  while y < len(list):
    if list[x] == 2 and list[y] == 2:
      return True
    else:
      y = y + 1
      x = x + 1
  return False
