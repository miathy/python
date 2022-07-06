def cheer(n):
    if n == 0:
        print('Hurray')
    else:
        print('Hip', end=' ')
        cheer(n-1)
    
cheer(3)