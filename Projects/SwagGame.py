#Game for Dean
#WORD
#Basic battle system with a dice-rolling system (requires a 20-sided dice, or d20 emulator)
#Small element of battle strategy (using the input 21 to regain health)
#basic winner or loser
#variable number of enemies
#randomly-generated enemy attack damage

from random import randint
swag = 50
enemies = 2
enswag = 25
print 'Woah, dawg! Some dudes just stole your swag! \nYou used to have 100, but now you have 50!'
raw_input('Press <<enter>> to continue..')
print '\nShow those punks who\'s boss.. roll a D20 to out-swag your opponents.'
raw_input('Press <<enter>> to continue..')
print '\nEnter the value "21" to sip some anti-haterade and restore some swag.'
raw_input('Press <<enter>> to continue..')
print '\nHere they come... defeat them both!\n'

while swag > 0 and enemies > 0:
	while enswag > 0 and swag > 0:
		print '\n\nRoll the dice to swag them! \nYour swag is at ' + `swag` + ' and the enemy in front of you has ' + `enswag` + ' swag.'
		hit = input('>>')
		if hit == 0:
			print '\nMan your swag is weak. Your enemy laughs in your face and takes no damage.'
		elif hit <= 6:
			print '\nYour swag slightly stuns the enemy, their swag is now at ' + `(enswag-hit)` + '.'
			enswag = enswag - hit
		elif hit <=12:
			print '\nYour swag damages the enemy, their swag is now at ' + `(enswag - hit)` + '.'
			enswag = enswag - hit
		elif hit <=19:
			print '\nThe enemy is crippled by your swag levels! Their swag is now at ' + `(enswag - hit)` + '.'
			enswag = enswag - hit
		elif hit == 20:
			print '\nSWAG OVERLOAD. Your enemy almost vaporizes from your swagtasticness!'
			enswag = 0
		elif hit == 21:
			print '\nSip that shit. Your swag increases from ' + `swag` + ' to ' + `(swag+15)` + '.'
			swag = swag + 15
		else:
			print '\nWhat? That\'s not a valid input. I guess you want to skip your turn, sucka!'

		if enswag > 0:		
			enhit = randint(0,20)
			if enhit == 0:
				print 'THAT PUNK AINT GOT SWAG. You laugh in their face and call their mother a fat whore.\n'
			elif enhit <= 6:
				print 'The enemy weakly swags all over the place. \nSome of it hits your face for ' + `enhit` + ' damage and your swag is now ' + `(swag-enhit)` + '.\n'
				swag = swag - enhit
			elif enhit <=12:
				print 'The enemy uses your stolen swag against you! \nThey hit you for ' + `enhit` + ' and your swag is now ' + `(swag - enhit)` + '.\n'
				swag = swag - enhit
			elif enhit <=19:
				print 'You take a direct hit from their funky swag, and boy does it stink.\nYou were hit for ' + `enhit` + ' points. You now have  ' + `(swag - enhit)` + ' swag.\n'
				swag = swag - enhit
			elif enhit == 20:
				print 'SWAG-AGEDDON! The swag of the enemy rains down on you like the wrath of Zeus!\nYou were hit for ' + `enhit` + ' points.You now have ' + `(swag - enhit)` + ' swag.\n'
				swag = swag - 30

		if enswag <= 0:
			print 'The enemy falls to the ground, overwhelmed by your swagger.\n'
			enemies = enemies - 1
			if enemies > 0:
				print 'A new enemy steps forward with full health!\n\n'
				enswag = 25

if enemies == 0:
	print 'Congratulations! You have defeated the posers. Flaunt your swag, brotato-chip. \nYou are a champ!!!'

else:
	print 'The swag drains from your body. You\'re a loser. Go cry in the corner.'

raw_input('Press <<enter>> to exit the game.')