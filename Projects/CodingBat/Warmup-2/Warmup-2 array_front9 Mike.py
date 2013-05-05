def array_front9(nums):
  x = 0
  tally = 0
  while x <= 3 and x <= len(nums)-1:
    if nums[x] == 9:
      tally = tally + 1
    x = x + 1
  if tally > 0:
    return True
  else:
    return False