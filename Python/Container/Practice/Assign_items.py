import random

i = random.randint(1, 6) #each office can be assigned at least one item
j = random.randint(1, 7-i)


name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

random.shuffle(name_list)

office1 = name_list[0:i]

temp_list = name_list[i:]

office2 = temp_list[0:j]

office3 = temp_list[j:]

print(office1)
print(office2)
print(office3)
