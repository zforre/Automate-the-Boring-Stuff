# 1. What is []?
# [] is a list
# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
# spam = [2,4,6,8,10]
# spam[2] = 'hello'
# print(spam)

# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
spam = ['a', 'b', 'c', 'd']
# 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
# evaluates to 'd'
# 4. What does spam[-1] evaluate to?
# evaluates to d
# 5. What does spam[:2] evaluate to?
# evaluates to ['a','b']

# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
bacon = [3.14, 'cat', 11, 'cat', True]
# 6. What does bacon.index('cat') evaluate to?
# evaluates to 1
# 7. What does bacon.append(99) make the list value in bacon look like?
# [3.14, 'cat', 11, 'cat', True, 99]
# 8. What does bacon.remove('cat') make the list value in bacon look like?
# [3.14, 'cat', 11, 'cat', True]
# bacon.remove('cat')
# print(bacon)
# [3.14, 11, 'cat', True]
# 9. What are the operators for list concatenation and list replication?
# + and *
# 10. What is the difference between the append() and insert() list methods?
# append adds to the end of list insert lets you choose where you want to add it
# 11. What are two ways to remove values from a list?
# using .remove() method or del list[index]
# 12. Name a few ways that list values are similar to string values.
# you can use list methods on strings you can concatenate both
# 13. What is the difference between lists and tuples?
# lists are mutable tuples are immutable
# 14. How do you type the tuple value that has just the integer value 42 in it?
# (42,)
# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
# tuple() and list() methods
# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# they contain references to the list
# 17. What is the difference between copy.copy() and copy.deepcopy()?
# copy.copy() copies a list copy.deepcopy() can copy a list within a list 