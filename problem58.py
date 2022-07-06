def bubbleSort(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)
    return lst


bubbleSort([2,1,3,5,2,7,4,9])