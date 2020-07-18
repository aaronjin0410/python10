import random

secret = random.randint(1, 10)
number = 0

while number < 3:
    guess = int(input('What Im thinking of: '))

    if guess > secret:
        print('higher')
    elif guess < secret:
        print('lower')
    else:
        print(f'Im thinking of {secret}, you are right!')
        break

    number += 1
else:
    print('Run out of times')

print('Game Over')
