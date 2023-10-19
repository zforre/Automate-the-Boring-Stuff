pets = ['cat', 'dog', 'bird', 'fish']

# access items in a list using its index [0]
print(pets[0])
print(pets[-1])
print(f'The {pets[0]} is afraid of the {pets[-1]}')

#slice: new list of items in defined range
print(pets[1:3])

nested = [['bob', 'jon', 'don'], [10, 20, 30, 40, 50]]

print(nested[0][0])
print(nested[1][0])

spam = ['cat', 'bat', 'rat', 'elephant']

# remove item from list (unassignment)
del spam[3]

print(spam)

print(len(spam))

# cancatenate lists
print(pets + spam)

# print(spam * 3)

#  list function turns value to list
print(list('hello'))

print('cat' in spam)
print('cat' not in spam)