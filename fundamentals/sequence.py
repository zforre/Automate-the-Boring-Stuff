# strings are like lists, they are an ordered sequence of values
# the things you can do with lists can also be done with strings

name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' in name)

for i in name:
    print(f'*** {i} ***')

# lists and strings are different in an important way
# list values are mutable strings are immutable
# mutable data type: it can have values added, removed, or changed.
# immutable: it cannot be changed. Trying to reassign a single character in a string results in a TypeError

#throws and error because strings are immutable
# name2 = 'Zophie a cat'
# name2[7] = 'the'
# print(name2)

# changes the string with concatenantion
name2 = 'Zophie a cat'
newName = f'{name[0:7]} the {name2[9:12]}'
print(name2)
print(newName)

