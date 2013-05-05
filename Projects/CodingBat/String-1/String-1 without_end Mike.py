def without_end(str):
  if len(str) == 2:
    return ""
  else:
    answer = str[1:(len(str)-1)]
    return answer
