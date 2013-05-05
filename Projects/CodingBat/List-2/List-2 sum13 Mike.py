def sum13(nums):
  list = nums
  x = 0
  sum = 0
  while x < len(list):
    if list[x] == 13:
      x = x + 2
    else:
     sum = sum + list[x]
     x = x + 1
  return sum
