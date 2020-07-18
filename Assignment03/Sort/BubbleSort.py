list = list(eval(input('pls input numbers: ')))
count = len(list) - 1

for i in range(count):
    for j in range(count - i):
        if list[j] > list[j + 1]:
            temp = list[j + 1]
            list[j + 1] = list[j]
            list[j] = temp

print(list)
