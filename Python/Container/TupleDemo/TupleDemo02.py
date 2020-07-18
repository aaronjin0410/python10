list1 = ['a', 'b', 'c', ('a', 'b')]
count = 0

for i in list1:
    if isinstance(i, tuple):
        break

    count += 1

print(count)
