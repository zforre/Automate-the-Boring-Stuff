eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

# Tuples are immutable. Tuples cannot have their values modified, appended, or removed.

# throws an error because the tuple spam is immutable
# spam = ('hello', 42, 0.5)
# eggs[1] = 99

# The comma is what lets Python know this is a tuple value
print(type(('hello',))) # tuple
print(type(('hello'))) # str

# You can use tuples to convey to anyone reading your code
# that you don’t intend for that sequence of values to change.
# If you need an ordered sequence of values that never changes,
# use a tuple.