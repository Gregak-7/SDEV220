#Name: Greg Kocal
#Version: Python 3
#Purpose of Life: Choose a number between 1 and 10 and assign it to the variable secret. Then, select another number 
#between 1 and 10 and assign it to the variable guess. Next, write the conditional tests (if, else, and elif) to print the string 
#'too low' if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret.

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
