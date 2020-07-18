size = int(input('pls input the size of square: '))

for row in range(size):
    for col in range(size):
        if row == 0 or row == size - 1:
            print('*', end=' ')
        else:
            if col == 0 or col == size - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()
