size = int(input('size of triangle: '))
row = 1

while row <= size:
    col1 = 1
    while col1 <= size - row:
        print(' ', end=' ')
        col1 += 1
    col2 = 1
    while col2 <= 2 * row - 1:
        if col2 == 1 or col2 == 2 * row - 1 or row == size:
            if row == size:
                if col2 % 2 != 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            else:
                print('*', end=' ')
        else:
            print(' ', end=' ')
        col2 += 1
    print()
    row += 1
