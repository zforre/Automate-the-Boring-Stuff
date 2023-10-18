name = 'Alice'

if name == "Alice" :
    print('Hi Alice')

print('Done')    

password = 'swordfish'

if password == 'swordfish':
    print('Access granted')
else:
    print('Access Denied')

name = 'bob'
age = 3000

if name == 'Alice':
    print('Hello Alice')
elif age < 20:
    print('You are not Alice')
elif age > 2000:
    print('Unlike you, Alice is not a vampire')
elif age > 100:
    print('You are not Alice, grannie')

name = input('Enter a name ')

if name:
    print('Hi ' + name + ', thanks for entering your name.')
else:
    print('You did not enter a name')
