#This program says hello and asks for your name and age
print('hello world')

print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)

print('The length of your name is: ' + str(len(myName)))

print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in around a year')
