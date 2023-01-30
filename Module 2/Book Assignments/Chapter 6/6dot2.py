#Name: Greg Kocal
#Version: Python 3
#Purpose of Life: Assign the value 7 to the variable guess_me, and the value 1 to the variable number. Write a while loop that compares 
#number with guess_me. Print 'too low' if number is less than guess me. If number equals guess_me, print 'found it!' and then exit the loop. 
#If number is greater than guess_me, print 'oops' and then exit the loop. Increment number at the end of the loop.

guess_me = 7
number = 0

while number <= guess_me:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1
    
    
    *******
    #Bug Report:
    #None to report
