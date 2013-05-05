def make_ends(nums):
  x=nums
  if len(x) == 1:
    z=[x[0],x[0]]
    return z
  else:
    z=[x[0],x[len(x)-1]]
    return z
