import copy

spam = ['a', 'b', 'c', 'd']
print(id(spam))

cheese =  copy.copy(spam) # copy module creates a new version incase you do not want to change the original
print(id(cheese)) # cheese is a different list with different identity.

cheese[1] = 42

print(spam)
print(cheese)

# Now the spam and cheese variables refer to separate lists, which is why only the list in cheese is modified when you assign 42 at index 1.