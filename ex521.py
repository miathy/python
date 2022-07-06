def pair(l1,l2,n):
    for i in l1:
        for j in l2:
            if i+j == n:
                print(i,j)

pair([2,3,4],[5,7,9,12],9)