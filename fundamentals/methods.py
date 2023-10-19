# PAGES 89-92

# index method returns index of item in list
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

# append method adds item to end of list
spam.append('hola')

# insert method adds item at defined input of a list
spam.insert(0, 'hallo')

# remove method removes item from list
spam.remove('hallo')

print(spam)

nums = [55, 2, 46, 3.14, 300, .50, 22, 0, -2]

# sort method puts items in order
nums.sort()
print(nums)

animals = ['dogs', 'ants', 'badgers', 'cats', 'elephants']
animals.sort()
# both do the same 
# animals.sort(reverse=True)
animals.reverse()
print(animals)

letters = ['a', 'Z', 'f', 'Q']
letters.sort(key=str.lower)
print(letters)