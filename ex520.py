def intersect(l1,l2):
    lst = []
    for i in l1:
        for j in l2:
            if i==j:
                lst.append(i) 
    print(lst)

intersect([1,2,3],[3,4,5])