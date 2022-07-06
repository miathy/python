
def print2D(t):
    for row in t:
        for item in row:
            print(item, end=' ')
        print()

def incr2D(t):
    nrows = len(t)  
    ncols = len(t[0])
    for i in range(nrows):
        for j in range(ncols):
            t[i][j]+=1

t= [[1,2,3],[4,5,6],[7,8,9]]

incr2D(t)  
print2D(t)