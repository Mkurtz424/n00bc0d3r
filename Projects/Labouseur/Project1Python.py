print 'Please enter the number of US cents you would like to make coins for: '
number = input('>> ')
quarters = 25
dimes = 10
nickles = 5
pennies = 1
num_quarters = 0
num_dimes = 0
num_nickles = 0
num_pennies = 0
if (number/quarters) >= 1:
  num_quarters = number/quarters
  number = number - (quarters*(number/quarters))
if (number/dimes) >= 1:
  num_dimes = number/dimes
  number = number - (dimes*(number/dimes))
if (number/nickles) >= 1:
  num_nickles = number/nickles
  number = number - (nickles*(number/nickles))
if number/pennies >= 1:
  num_pennies = number/pennies
  number = number - (pennies*(number/pennies))
print "Thank you! Change for your value comes to..."
print "Quarters: %d" % num_quarters
print "Dimes: %d" % num_dimes
print "Nickles: %d" % num_nickles
print "Pennies: %d" % num_pennies
raw_input('Press <<enter>> to close.')