def fix_teen(n):
  if n >= 13 and n <=19 and n!= 15 and n!=16:
    return 0
  else:
    return n
    
def no_teen_sum(a, b, c):
  noteensum = 0
  x = fix_teen(a)
  noteensum = noteensum+x
  x = fix_teen(b)
  noteensum = noteensum+x
  x = fix_teen(c)
  noteensum = noteensum+x
  return noteensum



  