def array123(nums):
  x=0
  tally = 0
  while x <= len(nums)-3:
    if nums[x] == 1:
      if nums[x+1] == 2:
        if nums[x+2] == 3:
          tally = tally + 1
          x = x+1
        else:
          x = x+1
      else:
        x = x+1
    else:
      x = x+1
  if tally >= 1:
    return True
  else:
    return False