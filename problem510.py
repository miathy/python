def interest(rate):
    amount = 100
    count = 0
    while amount <200:
        count += 1
        amount += amount*rate
    print(count)
    return count 


interest(0.07)