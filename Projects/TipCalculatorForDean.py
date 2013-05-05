"""
YO BRO
LET'S COMMENT ON SOME SHIT UP IN HERE.
This is a simple tip calculator!
It asks the end-user for the following:
-Meal Cost
-Desired Tip Percentage
It then gives the user this information:
-Tip Amount
-Total Meal Cost
It also asks if the user would like to
run the program again. If the user says
'Q', then it will not.
"""

print 'Welcome to the EZ-TIP calculator!'
print 'Let us begin...'
raw_input('Press <<enter>> to begin.')

while 1:
        mealcost = input('Please enter the meal cost, including tax: $')
        percentage = input('Please enter the tip percantage, e.g. "20" or "15": ')
        #
        tipmultiplyer = (percentage*.01)
        tipamount = (tipmultiplyer*mealcost)
    	tipamountround = round(tipamount,2)
        #
        totalmeal = mealcost + tipamountround
        print '...\n...\n...\nYour tip is %s, and your total meal cost is %s.' % (tipamountround,totalmeal)
        #
        cont=raw_input('Calculate another meal cost? Hit <<enter>>. Quit? Type \'Q\' and hit <<enter>>')
        #
        if cont == 'Q': break
