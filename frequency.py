students = ['Cindy', 'John', 'Cindy', 'Adam', 'Adam', 'Jimmy','Joan','Cindy','Joan']

def frequency(itemList):
    counters = {}
    for item in itemList:
        if item in counters:
            counters[item] += 1
        else:
            counters[item] = 1
    return counters
    #print(counters)

frequency(students)