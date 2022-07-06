def recNeg(lst):
    if lst[0] ==0:
        return False
    return recNeg(lst[:-1]) or lst[-1]<0

recNeg([1,2,-3])