def recursion(n):
    if n == 0:
        print(0, end = ' ')
    else:
        recursion(n-1)
        print(n, end = ' ')
        recursion(n-1)

recursion(3