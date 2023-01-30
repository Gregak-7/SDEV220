#Name: Greg Kocal
#Version: Python 3
#Purpose of Life: Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable called number over range(10). 
#If number is less than guess_me, print 'too low'. 
#If it equals guess_me, print found it! and then break out of the for loop. If number is greater than guess_me, print 'oops' and then exit the loop.

guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
*******
#Bug Report
#No Bugs in the system... we live to fight another day
