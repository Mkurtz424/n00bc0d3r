prime1=[]
#prime1 is a list in which I will store prime numbers, X.

prime2=[]
#prime2 is a temporary list that stores numbers that cleanly divide the number in question, X.

x=100

y=99


while x > 0:
	while y > 0:
		if x%y == 0:
			prime2.append(y)
		y=y-1
	if sum(prime2[:]) == 1:
		prime1.append(x)
		prime2 = []
	prime2 = []
	x=x-1
	y=x-1
	

print prime1


raw_input('Press <enter> to close.')
#this closes the program.