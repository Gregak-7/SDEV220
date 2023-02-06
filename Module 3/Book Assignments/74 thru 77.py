#Greg Kocal
#Book Assignments 7.4-7.7



# 7.4 Make a list called things with these three strings as elements
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5 Capitalize the element in things that refers to a person and then print the list.
things[1] = things[1].capitalize()
print(things) # Output: ['mozzarella', 'Cinderella', 'salmonella']

# 7.6 Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print(things) # Output: ['MOZZARELLA', 'Cinderella', 'salmonella']

# 7.7 Delete the disease element from things and print the list.
things.remove("salmonella")
print(things) # Output: ['MOZZARELLA', 'Cinderella']
