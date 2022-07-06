#def inBoth(l1,l2):

 #   if any(x in l1 for x in l2):
  #     print('true')
   # else:
    #    print('false')

#inBoth([1,2,3],[2,5,6])
def inBoth2(l1,l2):
    result=[]
    for n in l1:
        if n in l2:
            result.append(n)
        return result
    print(result)

inBoth2([1,2],[2,3,4])