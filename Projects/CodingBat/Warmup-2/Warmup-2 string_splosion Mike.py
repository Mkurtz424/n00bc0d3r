def string_splosion(word):
  result = ""
  x = 1
  while x <= len(word):
    result = result + word[:x]
    x+=1
  return result
