size = int(input('size of rhombus: '))

row1 = 1

while row1 <= size:
    col1 = 1
    while col1 <= size - row1:
        print(' ', end=' ')
        col1 += 1
    col2 = 1
    while col2 <= 2 * row1 - 1:
        if col2 == 1 or col2 == 2 * row1 - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
        col2 += 1
    row1 += 1
    print()

row2 = 1

while row2 <= size - 1:
    col3 = 1
    while col3 <= row2:
        print(' ', end=' ')
        col3 += 1
    col4 = 1
    while col4 <= 2 * (size - row2) - 1:
        if col4 == 1 or col4 == 2 * (size - row2) - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
        col4 += 1
    row2 += 1
    print()
