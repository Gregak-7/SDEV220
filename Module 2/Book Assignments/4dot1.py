secret = 5
guess = int(input("Guess a number between 1 and 10: "))

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")