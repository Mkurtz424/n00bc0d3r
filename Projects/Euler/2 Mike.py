fib = [2]
x = 1
y = 2
z = 0
while x<=4000000:
	z = x+y
	if z%2 == 0:
		fib.append(z)
	x = y
	y = z
print sum(fib[:])

raw_input('Press <enter> to exit.')
