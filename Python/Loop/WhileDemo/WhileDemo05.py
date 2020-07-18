row = 1

while row < 5:
    col = 1
    while col < 5:
        if col <= 4 - row:
            print(' ', end=' ')
        else:
            print('*', end=' ')
        col += 1
    row += 1
    print()