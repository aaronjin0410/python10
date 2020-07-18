list = list(eval(input('pls input numbers: ')))

count = len(list) - 1

for i in range(count):
    min_index = i
    for j in range(i + 1, count + 1):
        if list[min_index] > list[j]:
            min_index = j

    temp = list[i]
    list[i] = list[min_index]
    list[min_index] = temp

print(list)
