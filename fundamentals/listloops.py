nums = [0, 1, 2, 3, 4, 5]

# prints each index of i 
for i in nums:
    print(i)

# creates list of ints from 0 to 100 in increments of 2
hundedBy2 = list(range(0, 100, 2))

# print(hundedBy2)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders' ]

# range len function for returning int index and values inside
for i in range(len(supplies)):
    print(f'index {str(i)} in supplies is: {supplies[i]}')

# multiple assignments trick (assigns list items to defined variables)
cat = ['fat', 'black', 'sleepy']
size, color, disposition = cat

# swap operations
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a)
print(b)

# augmented assignment operators (+=, -=, *=, /=, %=)
spam = 42
spam += 1
print(spam)