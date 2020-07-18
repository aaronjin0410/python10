def hanoi(n, x, y, z):#将 n 个盘子从 x 移动到 y
    if n == 1:
        print(f'{x} ---> {z}')
    else:
        hanoi(n-1, x, z, y)#将 n-1 个盘子从 x 移动到 y
        print(f'{x} ---> {z}')
        hanoi(n-1, y, x, z)#将 n-1个盘子从 y 移动到 z



hanoi(8, 'x', 'y', 'z')
