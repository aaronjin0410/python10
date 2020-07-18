name_list = ['a', 'a', 'a', 'a']
j = 0

for i in range(len(name_list)):
    if name_list.index('a', j) >= 0:
        print(name_list.index('a', j))
        i += 1
    j += 1



