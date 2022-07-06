names = input('enter names:').split(',')
for name in names:
    if name[0].lower() in 'abcdefghijkl':
        print(name)