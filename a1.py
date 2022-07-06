def fact(n):
    if n==1:

        return 1
    else:
        r=n*fact(n-1)
        return n*fact(n-1)
        print(r)
    
fact(3)