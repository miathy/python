def recSum(lst):
    if len(lst)==0:
        return 0
    return recSum(lst[:-1]) +lst[-1]

recSum([1,2,3])

