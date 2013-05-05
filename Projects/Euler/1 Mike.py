x = 999
sum = 0

while x >= 0:
	if x%5 == 0 or x%3 == 0:
		sum = sum + x
	x = x-1

print sum

raw_input('Press <enter> to close.')