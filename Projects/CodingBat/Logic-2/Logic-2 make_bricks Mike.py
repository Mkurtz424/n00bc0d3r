def make_bricks(small, big, goal):
  if goal <= (small*1 + big*5):
    if goal%5 <= small:
      return True
    else:
      return False
  else:
    return False
