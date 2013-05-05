def max_end3(nums):
  x = nums
  if x[0] >= x[2]:
    x[2] = x[0]
    x[1] = x[0]
    return x
  else:
    x[0] = x[2]
    x[1] = x[2]
    return x
