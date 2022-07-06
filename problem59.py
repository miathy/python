def add2D(lst1, lst2): 
    for i in range(len(lst1)):
        for j in range(len(lst1[0])):
            lst1[i][j] +=lst2[i][j]
    print(lst1)

t = [[4,7,2,5],[5,1,9,2]]
s= [[0,1,2,0],[0,1,1,1]]
add2D(t,s)