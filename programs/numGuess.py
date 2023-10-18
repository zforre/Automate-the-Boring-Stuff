import random

name = input("What is your name? ")
secretNumber = random.randint(1, 20)
print(f'well, {name}, I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print("Too high")
    else:
        break

if guess == secretNumber:
    print(f'Good job {name}! You guessed correctly, that took {str(guessesTaken)} guesses!')
else:
    print(f'Sorry the number I was thinking of was {str(secretNumber)} try again?')