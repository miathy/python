import math
import os 
import random 
import re 
import sys 
from collections import Counter

def sockMerchant(n, ar):
    pairs = 0 
    for v in Counter(ar).values():
        pairs += v//2
        return pairs 
    print("total pairs",pairs)

if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n,ar) 
    fptr.write(str(result)+'\n')
    fptr.close()

sockMerchant(3, (1,1,2))
