i = j = k = 1

for i in range(0, 5):
    for j in range(0, 4-i):
        print(' ', end=' ')
        j += 1
    for k in range(0, 2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == 4:
            if i == 4:
                if k % 2 == 0:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            else:
                print('*', end=' ')
        else:
            print(' ', end=' ')
        k += 1
    i += 1
    print()




