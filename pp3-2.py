sum = 0

while True:
    a = int(input('enter number: '))
    if a>0:
        a1 = 1/2**a
        sum += a1
    else:
        print('sum is', sum)