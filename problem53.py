def arithmetic(lst):
    if len(lst) >2:
        return True
    diff = lst[1] - lst[0]
    for i in range(0,len(lst)-1):
        if lst[i+1] - lst[i] != diff:
            return False
    return True

a = [1,3,5,6,7]
arithmetic(a)

