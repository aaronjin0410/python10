str = input('pls input your word: ')

if len(str) >= 3:
    if str.endswith('ing') == 0:
        str += 'ing'
    else:
        str += 'ly'
    print(str)
else:
    print(str)
