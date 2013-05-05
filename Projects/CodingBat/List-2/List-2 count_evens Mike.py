def count_evens(nums):
  evencount = 0
  x = 0
  while x < len(nums):
    if nums[x] % 2 == 0:
      evencount = evencount + 1
      x = x + 1
    else:
      x = x + 1
  return evencount
