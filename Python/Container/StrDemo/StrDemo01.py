str = input('pls input any words: ')
sub_str = input('pls input substring: ')

i = 0
count = 0

while i < len(str):
    if str.find(sub_str, i, i + len(sub_str)) != -1:
        count += 1
    i += 1

print(count)
