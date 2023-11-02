# spam = {'color':'red', 'age': 42}

# for v in spam.values():
#     print(v)

# for k in spam.keys():
#     print(k)

# for i in spam.items():
#     print(i)

# print(spam.keys())
# print(list(spam.keys()))

# for k, v in spam.items():
#     print(f'Key: {k} Value: {str(v)}')

spam = {'name': 'Kewpie', 'age': 2}

# print('name' in spam.keys())
# print('Kewpie' in spam.values())
# print('color' in spam.keys())
# print('color' not in spam.keys())

# get() method
picnicItems = {'apples':5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# setdefault() method
spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))
print(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)