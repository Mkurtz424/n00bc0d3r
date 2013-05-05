def not_string(str):
  if str[0:3] == 'not':
      return str
  else:
      not_new = 'not ' + str
      return not_new
