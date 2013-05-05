def cat_dog(str):
  dogtally = 0
  cattally = 0
  x = 0
  y = 3
  while y <= len(str):
    if str[x:y] == "cat":
      cattally = cattally + 1
      x = x + 1
      y = y + 1
    elif str[x:y] == "dog":
      dogtally = dogtally + 1
      x = x + 1
      y = y + 1
    else:
      x = x + 1
      y = y + 1
  if cattally == dogtally:
    return True
  else:
    return False