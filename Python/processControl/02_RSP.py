import random

player = int(input('Please input your hand (1 for rock, 2 for scissor, 3 for paper): '))
comp = random.randint(1, 3)

if player == comp:
    print(f'player {player} comp {comp}, tie!')
elif (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
    print(f'player {player} comp {comp}, player wins!')
else:
    print(f'player {player} comp {comp}, comp wins!')

