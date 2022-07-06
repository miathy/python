def acronym(pharse):
    res = ''
    for char in pharse.split():
        res = char[0].upper()
        print(res,end='n')

acronym(' A b c')