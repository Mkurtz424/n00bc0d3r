def xyz_there(str):
  a=0
  b=1
  c=4
  if len(str) <= 3:
    if str == "xyz":
      return True
    else:
      return False
  while c<= (len(str)):
    if str[0:3] == "xyz":
      return True
    elif str[b:c] == "xyz":
      if str[a] != ".":
        return True
      else:
        a = a + 1
        b = b + 1
        c = c + 1
    else:
      a = a + 1
      b = b + 1
      c = c + 1
  return False