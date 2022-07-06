def fractorial(n):
    res = 1
    for i in range(2,n+1):
        res*=i
    print(res) 
    return res

fractorial(5)
