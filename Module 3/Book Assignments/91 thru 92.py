#Greg Kocal
#Book Assignments 9.1 - 9.2



# 9.1 Define a function called good()
def good():
    return ['Harry', 'Ron', 'Hermione']

# 9.2 Define a generator function called get_odds()
def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i

# Use a for loop to find and print the third value returned
for i, value in enumerate(get_odds()):
    if i == 2:
        print(value) # Output: 5
        break
