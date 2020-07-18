import random
player = int(input('1 for rock, 2 for scissor, 3 for paper, plz show your hand: '))
computer = random.randint(1,3)

if player == computer:
    print(f'player: ')