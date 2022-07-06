def doubles(x):
    for i,a in enumerate(x[:-1]):
        if x[i+1] == a*2:
            print(a*2)

#def doubles(x):
 #   for i in x:
  #      if i+1 = 2*i 
   #     print(i)
doubles([3,0,1,2,3,6,2,4,5,6,5])