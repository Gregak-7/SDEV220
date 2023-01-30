#Name Greg Kocal
#Version Python 3
secret = 5
guess = int(input("Guess a number between 1 and 10: "))

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")
    
    
    
    *********************
    #Bug Report
    #Mispelled elif... not my proudest moment... elif - not elsif
