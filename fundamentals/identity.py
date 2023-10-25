print(id("howdy"))

# bacon is a string so it's immutable (if it is changed it creates a new string therefore creating a new id)
bacon = 'Hello'
print(id(bacon))

bacon += ' world!'
print(id(bacon))

eggs = ['cat', 'dog'] # This creates a new list.
print(id(eggs))

eggs.append('moose') # append() modifies the list "in place"
print(id(eggs)) # eggs still refers to the same list as before.

eggs = ['bat', 'rat', 'cow'] # this creates a new list with a new id
print(id(eggs)) # eggs now refers to a completely different list.

# The append(), extend(), remove(), sort(), reverse(), and other list methods modify their lists in place.