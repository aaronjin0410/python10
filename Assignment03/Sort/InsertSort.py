list = list(eval(input('pls input numbers: ')))
count = len(list) - 1

for i in range(count):
    for j in range(i + 1):
        if list[i + 1] < list[j]:
            temp = list.pop(i + 1)
            list.insert(j, temp)

print(list)
