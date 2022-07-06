def xmult(lst1,lst2):
    lst = []
    for i in lst1:
        for j in lst2:
            new = i*j
            lst.append(new)
    print(lst)
    return lst

#xmult([2],[1,5])
xmult([3,5],[3,11])