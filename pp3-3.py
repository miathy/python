n =int(input('enter number of time you have run around a racetrack: '))
l =[]
for i in range(1, n+1):
    i= int(input('enter the lap time:'))
    l.append(i) 
print(max(l))
print(min(l))
     