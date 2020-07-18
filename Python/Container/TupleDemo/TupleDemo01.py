tuple1 = ('B', 'y', 't', 'e', 'T', 'u', 'b', 'e')

i = tuple1.index('T')

left_tuple1 = tuple1[0:i]
right_tuple2 = tuple1[i + 1:]

tuple1 = left_tuple1 + right_tuple2

print(tuple1)
