def big_diff(nums):
  biglist = nums
  biglist.sort()
  return abs(biglist[0]-biglist[-1])
