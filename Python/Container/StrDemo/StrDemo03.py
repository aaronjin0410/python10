str = input('pls input your word: ')
nth = int(input('pls input Nth char you\'d like to remove: '))

if len(str) > 0:
    left_str = str[:(nth - 1)]
    right_str = str[nth:]
    new_str = left_str + right_str
    print(new_str)
else:
    print('you got no word to say?')
