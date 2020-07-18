list1 = [5, 6, 3, 1]
for index, value in enumerate(list1):
    other = 10 - value
    if other in list1 and list1.index(other) != index:
        print(index, value)
        print(list1.index(other), other)
        break
