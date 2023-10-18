def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('You cannot divide by 0')

# try and except allows the program to continue running after error

print(div42by(12))
print(div42by(2))
print(div42by(1))
print(div42by(0)) #cannot divide by 0
print(div42by(3))

numCats = input("How many cats do you own? ")

try:
    if int(numCats) >= 4:
        print('wow thats a lot of cats')
    elif int(numCats) < 0:
        print('You cant have negative cats')
    else:
        print('you have a few cats')
except ValueError:
    print('You did not enter a number')
