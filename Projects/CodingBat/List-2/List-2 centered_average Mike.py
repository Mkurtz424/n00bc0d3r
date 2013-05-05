def centered_average(nums):
  list=nums
  list.sort()
  sum1 = sum(list[1:-1])
  sum2 = sum1/((len(list))-2)
  return sum2
